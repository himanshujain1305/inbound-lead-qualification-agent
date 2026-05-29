# n8n Workflow Plan

This document describes how the Inbound Lead Qualification Agent can be extended into a real automation workflow using n8n.

## Automation Goal

Move from a manual CSV upload workflow to an automated sales and marketing operations workflow.

The goal is to simulate how an inbound lead can move from form submission to sales-ready follow-up with minimal manual work.

## Proposed n8n Flow

Form Submission
↓
Lead Data Captured
↓
Lead Qualification Logic Runs
↓
High-Fit Leads Flagged
↓
CRM or Google Sheet Updated
↓
Follow-Up Email Draft Generated
↓
Sales Notification Sent

## Workflow Steps

1. Form Submission

A prospect submits a lead form with fields such as name, company, job title, company size, pain point, budget range, timeline, and lead source.

2. Lead Data Captured

n8n receives the form submission through a webhook or form trigger.

3. Lead Qualification Logic Runs

The lead data is sent to the Python qualification logic or an API endpoint that scores the lead and returns:

- Lead score
- Fit level
- Qualification reason
- Recommended next action
- Draft follow-up email

4. High-Fit Leads Flagged

If the lead is High fit, the workflow marks it as sales-priority.

5. CRM or Google Sheet Updated

The enriched lead record is added to a Google Sheet or CRM-style tracker.

6. Follow-Up Email Draft Generated

The generated email draft is stored with the lead record. In a future version, this can create a Gmail draft.

7. Sales Notification Sent

For High-fit leads, n8n can send a Slack or email notification to the sales owner.

## Business Value

This automation reduces manual lead review time, improves speed-to-lead, and gives sales teams a clearer view of which leads should be prioritized first.

## Future Implementation

Possible tools:

- n8n
- Google Forms or Typeform
- Google Sheets
- Gmail
- Slack
- Python API or lightweight webhook endpoint