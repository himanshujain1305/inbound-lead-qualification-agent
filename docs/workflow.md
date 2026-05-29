# Workflow Diagram

This project simulates an inbound lead qualification workflow for sales and marketing operations.

## Workflow

Inbound Lead CSV
↓
Lead Scoring Logic
↓
Fit Level + Qualification Reason
↓
Recommended Sales Action
↓
Draft Follow-Up Email
↓
CRM-Ready Output CSV
↓
Streamlit Demo + Download

## What Each Step Does

1. Inbound Lead CSV: Starts with lead information such as company, job title, company size, pain point, budget range, timeline, and lead source.

2. Lead Scoring Logic: Scores each lead based on company size, seniority, budget, and purchase timeline.

3. Fit Level + Qualification Reason: Classifies each lead as High, Medium, or Low fit and explains why.

4. Recommended Sales Action: Suggests whether to prioritize immediate outreach, nurture, or keep the lead lower priority.

5. Draft Follow-Up Email: Generates a lead-facing email draft based on the company, pain point, and fit level.

6. CRM-Ready Output CSV: Saves the enriched lead data into a final CSV output.

7. Streamlit Demo + Download: Lets users upload a CSV, view metrics, inspect leads, preview emails, and download the final CRM-ready file.