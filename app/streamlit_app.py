import sys
from pathlib import Path

import streamlit as st
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "app"))

from lead_scoring import qualify_leads
from email_generator import generate_follow_up


st.set_page_config(
    page_title="Inbound Lead Qualification Agent",
    layout="wide"
)

st.title("Inbound Lead Qualification Agent")
st.write("From raw inbound leads to sales-ready qualification, next actions, and follow-up drafts.")

st.markdown("### Try the demo")
st.write("Download the sample CSV first, then upload it below to test the workflow.")

sample_path = PROJECT_ROOT / "data" / "sample_leads.csv"

with open(sample_path, "rb") as file:
    st.download_button(
        label="Download Sample Leads CSV",
        data=file,
        file_name="sample_leads.csv",
        mime="text/csv"
    )

required_columns = [
    "lead_id",
    "first_name",
    "last_name",
    "company",
    "job_title",
    "company_size",
    "industry",
    "pain_point",
    "budget_range",
    "timeline",
    "source"
]

uploaded_file = st.file_uploader("Upload inbound leads CSV", type=["csv"])

if uploaded_file is not None:
    leads = pd.read_csv(uploaded_file)

    missing_columns = [col for col in required_columns if col not in leads.columns]

    if missing_columns:
        st.error("Your CSV is missing required columns.")
        st.write("Missing columns:")
        st.write(missing_columns)

        st.write("Required columns:")
        st.write(required_columns)

        st.stop()

    temp_path = PROJECT_ROOT / "data" / "uploaded_leads.csv"
    leads.to_csv(temp_path, index=False)

    qualified_leads = qualify_leads(temp_path)
    qualified_leads["draft_follow_up_email"] = qualified_leads.apply(generate_follow_up, axis=1)

    total_leads = len(qualified_leads)
    high_fit = len(qualified_leads[qualified_leads["fit_level"] == "High"])
    low_fit = len(qualified_leads[qualified_leads["fit_level"] == "Low"])

    manual_minutes = total_leads * 10
    automated_minutes = total_leads * 1
    minutes_saved = manual_minutes - automated_minutes

    st.subheader("Workflow Impact")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Leads Processed", total_leads)
    col2.metric("High-Fit Leads", high_fit)
    col3.metric("Low-Fit Leads", low_fit)
    col4.metric("Minutes Saved", minutes_saved)

    st.subheader("Qualified Leads")

    display_columns = [
        "lead_id",
        "company",
        "job_title",
        "industry",
        "budget_range",
        "timeline",
        "lead_score",
        "fit_level",
        "recommended_next_action"
    ]

    st.dataframe(
        qualified_leads[display_columns],
        width="stretch",
        hide_index=True
    )

    st.subheader("Qualification Reason")
    selected_company = st.selectbox("Choose a company", qualified_leads["company"])
    selected_row = qualified_leads[qualified_leads["company"] == selected_company].iloc[0]

    st.write(selected_row["qualification_reason"])

    st.subheader("Follow-Up Email Preview")
    st.text_area("Draft Email", selected_row["draft_follow_up_email"], height=300)

    csv = qualified_leads.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CRM-Ready CSV",
        data=csv,
        file_name="final_qualified_leads.csv",
        mime="text/csv"
    )

else:
    st.info("Upload a CSV with the required columns, or download the sample file above to try the demo.")
