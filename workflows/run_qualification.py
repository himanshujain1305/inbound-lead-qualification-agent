from app.lead_scoring import qualify_leads
from app.email_generator import generate_follow_up


def main():
    scored_leads = qualify_leads("data/sample_leads.csv")
    scored_leads["draft_follow_up_email"] = scored_leads.apply(generate_follow_up, axis=1)

    output_path = "data/final_qualified_leads.csv"
    scored_leads.to_csv(output_path, index=False)

    print(f"Processed {len(scored_leads)} leads")
    print(f"Saved final CRM-ready file to: {output_path}")
    print()
    print(scored_leads[[
        "lead_id",
        "company",
        "lead_score",
        "fit_level",
        "recommended_next_action"
    ]])


if __name__ == "__main__":
    main()
