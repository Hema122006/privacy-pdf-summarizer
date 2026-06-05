import streamlit as st
from modules.pdf_extractor import extract_text
from modules.pii_detector import detect_pii
from modules.blur_generator import blur_text
from modules.summarizer import generate_summary
import os

st.set_page_config(
    page_title="Privacy-Preserving PDF Summarizer",
    layout="wide"
)

st.title("📄 Privacy-Preserving PDF Summarizer")

uploaded_file = st.file_uploader(
    "Upload a PDF File",
    type=["pdf"]
)

if uploaded_file:

    # Save uploaded PDF
    save_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF Uploaded Successfully!")

    # Extract text from PDF
    text = extract_text(save_path)

    # Generate summary first
    summary = generate_summary(text)

    # Detect personal information in summary
    pii_entities = detect_pii(summary)

    protected_summary = blur_text(
        summary,
        pii_entities
    )

    # Extracted Text
    st.subheader("📄 Extracted Text")

    st.text_area(
        "Original PDF Content",
        text,
        height=250
    )

    # Generated Summary
    st.subheader("📝 Generated Summary")

    st.text_area(
        "Summary",
        summary,
        height=200
    )

    # Privacy Preserved Summary
    st.subheader("🔒 Privacy-Preserved Summary")

    st.text_area(
        "Protected Summary",
        protected_summary,
        height=200
    )

    # Download Summary
    st.download_button(
        label="📥 Download Summary",
        data=summary,
        file_name="summary.txt",
        mime="text/plain"
    )

    # Download Protected Summary
    st.download_button(
        label="📥 Download Protected Summary",
        data=protected_summary,
        file_name="protected_summary.txt",
        mime="text/plain"
    )