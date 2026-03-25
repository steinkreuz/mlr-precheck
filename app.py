import streamlit as st
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

# Steinkreuz Project #1: MLR-PreCheck
# Open-source Fair Balance and Off-Label Auditor

st.set_page_config(page_title="Steinkreuz | MLR-PreCheck", page_icon="🧬")

st.title("🧬 MLR-PreCheck")
st.subheader("Open-Source Oncology Compliance Auditor")
st.markdown("---")

with st.sidebar:
    st.header("About")
    st.info("Built by Steinkreuz — the open-source agentic factory for oncology pharma. [steinkreuz.org](https://steinkreuz.org)")
    st.caption("Set your ANTHROPIC_API_KEY in the .env file to run this tool locally.")

st.write("Paste the promotional text or clinical claim you wish to audit below.")
input_text = st.text_area("Promotional Content / Claim Text", height=200, placeholder="e.g., 'DRUG-X is the most effective 1L treatment for all NSCLC patients regardless of mutation status.'")

if st.button("Run Compliance Audit"):
    if not input_text:
        st.warning("Please enter some text to audit.")
    else:
        try:
            client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            with st.spinner("Analyzing against 21 CFR Part 202 and EU Directive 2001/83/EC..."):
                message = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1500,
                    system="You are a Senior MLR Compliance Officer specializing in Oncology. Audit the provided text for Fair Balance violations, off-label claims, and missing safety disclosures based on 21 CFR Part 202 and EU Directive 2001/83/EC. Output a clear PASS/FAIL, the specific regulation cited, and the recommended fix.",
                    messages=[
                        {"role": "user", "content": f"Audit this claim: {input_text}"}
                    ]
                )
                result = message.content[0].text
                if "FAIL" in result.upper():
                    st.error("🚨 AUDIT RESULT: FAIL")
                else:
                    st.success("✅ AUDIT RESULT: PASS")
                st.markdown("### Compliance Report")
                st.write(result)
        except Exception as e:
            if "529" in str(e) or "overloaded" in str(e).lower():
                st.warning("⏳ Anthropic API is temporarily busy. This is not an error with the tool — please wait 30 seconds and try again.")
            else:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Legal Disclaimer: This tool is for decision support only. Final approval must be granted by a qualified MLR professional.")