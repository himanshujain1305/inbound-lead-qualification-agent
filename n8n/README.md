# n8n Automation Layer

This folder documents the planned n8n workflow that extends the Inbound Lead Qualification Agent from a Streamlit MVP into a fully automated, event-driven sales operations pipeline.

## What This Adds

The Streamlit app handles CSV uploads and batch qualification manually. This n8n layer makes the same logic run automatically the moment a new lead comes in — no uploads, no manual steps.

| Streamlit MVP | n8n Automation Layer |
|---|---|
| Manual CSV upload | Webhook receives lead in real time |
| Run on demand | Triggered automatically on form submit |
| Results shown in browser | Results written to Google Sheets |
| Email draft displayed in UI | Gmail draft created in the sales inbox |
| No notifications | Slack alert sent for High-fit leads |

## Workflow Summary

```
Webhook Trigger
    ↓
Set / Transform Node  (normalize and enrich fields)
    ↓
IF Node              (fit_level == "High"?)
    ↓ Yes                          ↓ No
Google Sheets Append         Google Sheets Append
(priority queue tab)         (all leads tab)
    ↓
Gmail Node           (create draft follow-up email)
    ↓
Slack Node           (notify sales owner — High-fit only)
```

## Node Reference

| # | Node | Type | Purpose |
|---|------|------|---------|
| 1 | Inbound Lead Webhook | Webhook | Receives POST payload from form or API |
| 2 | Format Lead Fields | Set | Normalizes field names, adds `received_at` timestamp |
| 3 | Check Fit Level | IF | Routes High-fit leads to priority path |
| 4 | Append to Sheets (Priority) | Google Sheets | Writes High-fit leads to `High-Fit Queue` tab |
| 5 | Append to Sheets (All Leads) | Google Sheets | Writes every lead to `All Leads` tab |
| 6 | Create Gmail Draft | Gmail | Generates draft follow-up from template |
| 7 | Notify Sales via Slack | Slack | Posts summary card for High-fit leads |

## How to Use These Files

| File | Purpose |
|------|---------|
| `workflow-outline.md` | Full node-by-node configuration reference |
| `test-webhook-payload.json` | Sample POST body for testing the webhook trigger |

To test locally:
1. Import the workflow outline into n8n and configure each node.
2. Activate the workflow and copy the webhook URL.
3. Send `test-webhook-payload.json` via curl or Postman:

```bash
curl -X POST https://your-n8n-instance/webhook/inbound-lead \
  -H "Content-Type: application/json" \
  -d @test-webhook-payload.json
```

## Credentials Required (not included)

All credentials are managed inside n8n's credential store — nothing is hardcoded here.

| Service | n8n Credential Type | Scope Needed |
|---------|---------------------|--------------|
| Google Sheets | Google OAuth2 | spreadsheets |
| Gmail | Google OAuth2 | gmail.compose |
| Slack | Slack OAuth2 | chat:write |

## Business Impact

This layer eliminates the manual handoff between lead capture and sales action. For a team receiving 20 inbound leads per week, automating qualification, CRM entry, email drafting, and Slack notification saves an estimated 3–4 hours of SDR time per week and reduces speed-to-lead from hours to seconds.

## Portfolio Context

This workflow is designed to demonstrate marketing operations and RevOps automation skills relevant to roles including:
- Marketing Operations Analyst
- Growth Analyst
- GTM / Revenue Operations
- Sales Operations

The full qualification logic lives in `workflows/run_qualification.py`. The n8n layer is the integration shell that operationalizes it.
