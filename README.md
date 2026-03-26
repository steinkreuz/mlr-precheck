# 🧬 MLR-PreCheck

**Open-source AI agent that audits pharma promotional materials for FDA/EMA Fair Balance compliance violations — result in 30 seconds.**

Built by [Standard Agentics](https://standardagentics.org) — open-source agentic infrastructure for the full drug development journey.

---

## The Problem

Every pharma company risks FDA/EMA Warning Letters if promotional materials contain misleading claims, invisible safety text, or off-label suggestions. The current process is a human MLR reviewer checking each item manually. Cost: €2,000+/day. Speed: days per item.

## The Solution

A 30-second automated pre-check that flags violations before the human reviewer sees the material. Binary output: PASS or FAIL with the exact regulation cited and a recommended fix.

## What It Checks

- **Fair Balance violations** — safety information missing or minimised
- **Superlative claims** — "most effective", "best in class" without substantiation
- **Off-label suggestions** — claims outside the approved indication
- **Overly broad efficacy claims** — patient populations not matching the label

## Regulations Covered

- 21 CFR Part 202 (FDA — US promotional materials)
- EU Directive 2001/83/EC Articles 87 and 89

## How to Run

**Requirements:** Python 3.9+, an Anthropic API key
```bash
pip install streamlit anthropic
streamlit run app.py
```

1. Add your Anthropic API key to the `.env` file
2. Paste your promotional text or clinical claim
3. Click **Run Compliance Audit**
4. Receive PASS/FAIL with regulation cited and recommended fix

## Example Output

**Input:** "DRUG-X is the most effective first-line treatment for all NSCLC patients regardless of mutation status, with no serious side effects reported."

**Output:** FAIL
- Superlative Claim Without Substantiation (21 CFR 202.1(e)(6)(i))
- Overly Broad Efficacy Claim (21 CFR 202.1(e)(5)(i))
- Misleading Safety Statement (21 CFR 202.1(e)(5)(ii))
- Missing Fair Balance (21 CFR 202.1(e)(5)(i))

## License

MIT — free to use, fork, deploy, and audit the code.

---

*Legal Disclaimer: This tool is for decision support only. Final approval must be granted by a qualified MLR professional.*

*Built by [Standard Agentics](https://standardagentics.org) — open-source agentic infrastructure for the full drug development journey.*
