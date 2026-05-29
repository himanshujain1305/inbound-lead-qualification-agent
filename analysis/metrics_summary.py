import pandas as pd


def main():
    leads = pd.read_csv("data/scored_leads.csv")

    total_leads = len(leads)
    high_fit_leads = len(leads[leads["fit_level"] == "High"])
    medium_fit_leads = len(leads[leads["fit_level"] == "Medium"])
    low_fit_leads = len(leads[leads["fit_level"] == "Low"])

    manual_minutes_per_lead = 10
    automated_minutes_per_lead = 1

    manual_total_minutes = total_leads * manual_minutes_per_lead
    automated_total_minutes = total_leads * automated_minutes_per_lead
    minutes_saved = manual_total_minutes - automated_total_minutes

    qualification_rate = round((high_fit_leads / total_leads) * 100, 1)

    print("Inbound Lead Qualification Metrics")
    print("----------------------------------")
    print(f"Total leads processed: {total_leads}")
    print(f"High-fit leads identified: {high_fit_leads}")
    print(f"Medium-fit leads identified: {medium_fit_leads}")
    print(f"Low-fit leads identified: {low_fit_leads}")
    print(f"High-fit qualification rate: {qualification_rate}%")
    print()
    print("Time Savings Estimate")
    print("---------------------")
    print(f"Manual workflow time: {manual_total_minutes} minutes")
    print(f"Automated workflow time: {automated_total_minutes} minutes")
    print(f"Estimated time saved: {minutes_saved} minutes")
    print(f"Manual time per lead reduced from {manual_minutes_per_lead} minutes to {automated_minutes_per_lead} minute")


if __name__ == "__main__":
    main()
