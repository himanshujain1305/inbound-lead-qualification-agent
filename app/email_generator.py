import pandas as pd


def generate_follow_up(row):
    first_name = row["first_name"]
    company = row["company"]
    pain_point = row["pain_point"]
    fit_level = row["fit_level"]

    if fit_level == "High":
        cta = "Would you be open to a quick 15-minute conversation this week?"
        value_line = "This looks like the kind of workflow where faster lead qualification could save your team meaningful time."
    elif fit_level == "Medium":
        cta = "Would it make sense to send over a short example workflow?"
        value_line = "There may be an opportunity to make your follow-up process more structured without adding more manual work."
    else:
        cta = "Happy to stay connected if this becomes more relevant later."
        value_line = "Even if this is not urgent right now, having a simple qualification process can help when inbound volume increases."

    email = f"""Subject: Quick idea for {company}

Hi {first_name},

I noticed that your team may be dealing with: {pain_point}.

A simple lead qualification workflow could help your team quickly identify which inbound leads need immediate sales attention, which leads should go into nurture, and which ones are lower priority.

{value_line}

{cta}

Best,
Himanshu
"""

    return email


def add_follow_up_emails(input_path="data/scored_leads.csv"):
    leads = pd.read_csv(input_path)
    leads["draft_follow_up_email"] = leads.apply(generate_follow_up, axis=1)
    return leads


if __name__ == "__main__":
    leads_with_emails = add_follow_up_emails()
    print(leads_with_emails[["company", "fit_level", "draft_follow_up_email"]].head())
