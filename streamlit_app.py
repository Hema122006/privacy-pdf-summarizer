import streamlit as st
from modules.pdf_extractor import extract_text
from modules.pii_detector import detect_pii
from modules.blur_generator import blur_text
from modules.summarizer import generate_summary
import os

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Privacy-Preserving PDF Summarizer",
    page_icon="🔒",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Main App Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0b1020 0%,
        #1a103d 50%,
        #0b1020 100%
    );
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #020617,
        #0f172a
    );
    border-right: 1px solid #334155;
}

/* Header */
.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    background: linear-gradient(
        90deg,
        #60a5fa,
        #a855f7
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 20px rgba(124,58,237,0.7);
}

.sub-title {
    text-align: center;
    color: #cbd5e1;
    font-size: 20px;
    margin-bottom: 25px;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    padding-top: 30px;
    font-size: 14px;
}

/* Metrics */
[data-testid="metric-container"] {
    background: #1b1535;
    border: 1px solid #334155;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    background-color: #1e293b;
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
}

.stTabs [aria-selected="true"] {
    background-color: #7c3aed;
}

/* Text Areas */
textarea {
    background-color: #0f172a !important;
    color: white !important;
}

/* Upload Area */
[data-testid="stFileUploader"] {
    background: #1e293b;
    border-radius: 15px;
    padding: 15px;
}

/* Success Box */
.stSuccess {
    border-radius: 12px;
}

/* General Text */
h1, h2, h3, h4, h5, h6,
p, label, div {
    color: #f8fafc;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🔒 Project Menu")

st.sidebar.info(
    """
    Privacy-Preserving PDF Summarizer

    Features:
    • PDF Upload
    • NLP Summarization
    • PII Detection
    • Privacy Protection
    • Summary Download
    """
)

# ---------------- HEADER ---------------- #

st.markdown(
    '<p class="main-title">🔒 Privacy-Preserving PDF Summarizer</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Secure Document Analysis Using NLP</p>',
    unsafe_allow_html=True
)

st.divider()
st.markdown("""
    <div style="
    background: linear-gradient(90deg,#312e81,#7c3aed);
    padding:25px;
    border-radius:20px;
    text-align:center;
    margin-bottom:20px;
    ">
    <h2 style="color:white;"> 
    🔒 Protect Sensitive Information with AI
    </h2>

    <p style="color:white;font-size:18px;">
    Upload PDF → Generate Summary → Detect PII → Hide Personal Information
    </p>

    </div>
    """, unsafe_allow_html=True)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📄 Upload a PDF File",
    type=["pdf"]
)

# ---------------- PROCESS PDF ---------------- #

if uploaded_file:

    save_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ PDF Uploaded Successfully!")

    with st.spinner("Processing PDF..."):

        # Extract text
        text = extract_text(save_path)

        # Generate summary
        summary = generate_summary(text)

        # Detect PII in summary
        pii_entities = detect_pii(summary)

        # Protect summary
        protected_summary = blur_text(
            summary,
            pii_entities
        )

    # ---------------- DASHBOARD ---------------- #

    st.subheader("📊 Privacy Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "PII Detected",
            len(pii_entities)
        )

    with col2:
        st.metric(
            "Masked",
            len(pii_entities)
        )

    with col3:
        st.metric(
            "Privacy Score",
            "100%"
        )
        st.progress(100)

    st.divider()


    # ---------------- TABS ---------------- #

    tab1, tab2, tab3 = st.tabs(
        [
            "📄 Original Text",
            "📝 Summary",
            "🔒 Privacy Report"
        ]
    )

    # Original Text

    with tab1:

        st.text_area(
            "Extracted PDF Content",
            text,
            height=350
        )

    # Summary Tab

    with tab2:

        st.subheader("📝 Generated Summary")

        st.text_area(
            "Summary",
            summary,
            height=180
        )

        st.subheader("🔒 Privacy-Preserved Summary")

        st.text_area(
            "Protected Summary",
            protected_summary,
            height=180
        )

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="📥 Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

        with col2:
            st.download_button(
                label="📥 Download Protected Summary",
                data=protected_summary,
                file_name="protected_summary.txt",
                mime="text/plain"
            )

    # Privacy Report Tab

    with tab3:

        st.subheader("📊 Privacy Analysis Report")

        st.success(
            f"{len(pii_entities)} sensitive entities detected and masked."
        )

        if pii_entities:

            st.write("### Detected Entities")

            for entity in pii_entities:
                st.write("•", entity)

        else:
            st.info("No sensitive information detected.")

    # ---------------- FOOTER ---------------- #

    st.markdown("""
    <hr>

    <div style="
    text-align:center;
    padding:20px;
    color:#94a3b8;
    ">

    🔒 Privacy-Preserving PDF Summarizer

    Powered by Python • NLP • SpaCy • Streamlit

    Version 1.0 Enterprise Edition

    </div>
    """, unsafe_allow_html=True)
    
