import pandas as pd


def score_lead(row):
    score = 0
    reasons = []

    # Company size scoring
    if row["company_size"] in ["200-500", "500-1000", "100-200"]:
        score += 25
        reasons.append("Company size suggests a real sales/ops team with enough volume.")
    elif row["company_size"] == "11-50":
        score += 10
        reasons.append("Smaller company, possible fit but likely lower urgency.")
    else:
        reasons.append("Very small company, likely limited buying capacity.")

    # Job title scoring
    senior_titles = ["VP", "Director", "Head", "Founder"]
    if any(title in row["job_title"] for title in senior_titles):
        score += 25
        reasons.append("Lead has decision-maker or senior influencer title.")

    # Budget scoring
    if row["budget_range"] in ["$50k-$100k", "$25k-$50k"]:
        score += 25
        reasons.append("Budget range indicates potential buying capacity.")
    else:
        reasons.append("Budget appears limited.")

    # Timeline scoring
    urgent_timelines = ["Next 30 days", "Next 60 days", "This quarter"]
    if row["timeline"] in urgent_timelines:
        score += 25
        reasons.append("Timeline suggests near-term intent.")
    else:
        reasons.append("Timeline is vague or long-term.")

    if score >= 75:
        fit = "High"
        next_action = "Prioritize for sales outreach within 24 hours."
    elif score >= 40:
        fit = "Medium"
        next_action = "Add to nurture sequence and review manually."
    else:
        fit = "Low"
        next_action = "Keep in CRM, but do not prioritize immediate sales time."

    return pd.Series({
        "lead_score": score,
        "fit_level": fit,
        "qualification_reason": " ".join(reasons),
        "recommended_next_action": next_action
    })


def qualify_leads(input_path="data/sample_leads.csv"):
    leads = pd.read_csv(input_path)
    scored = leads.join(leads.apply(score_lead, axis=1))
    return scored


if __name__ == "__main__":
    result = qualify_leads()
    print(result[[
        "lead_id",
        "first_name",
        "last_name",
        "company",
        "lead_score",
        "fit_level",
        "recommended_next_action"
    ]])
