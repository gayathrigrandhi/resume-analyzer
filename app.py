import streamlit as st
import os

# Load CSS
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Imports
from nlp_engine.skill_extractor import extract_skills
from matcher.match_algorithm import calculate_match
from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text
from visualization.charts import skill_chart

UPLOAD_FOLDER = "uploads"

# Page settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Title
st.markdown(
"""
<h1 style='text-align:center;'>Smart ATS Resume Analyzer for Job Matcher</h1>
<p style='text-align:center; font-size:18px;'>
Analyze your resume against job descriptions and discover skill gaps instantly.
</p>
""",
unsafe_allow_html=True
)

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)

# Job Description
job_description = st.text_area(
    "Paste Job Description Here"
)

# If resume uploaded
if uploaded_file is not None:

    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume Uploaded Successfully!")

    # Extract text
    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_pdf_text(file_path)
    else:
        resume_text = extract_docx_text(file_path)

    st.subheader("Extracted Resume Text")
    st.text(resume_text)

    # Run analysis only if job description exists
    if job_description:

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)

        # Calculate match
        score, matched, missing = calculate_match(job_skills, resume_skills)

        # Show Resume & Job Skills in columns
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Resume Skills")
            for skill in resume_skills:
                st.success(skill.upper())

        with col2:
            st.subheader("Job Skills")
            for skill in job_skills:
                st.info(skill.upper())

        st.divider()

        # Matched Skills
        st.subheader("Matched Skills")
        for skill in matched:
            st.success(skill.upper())

        st.divider()

        # Match Percentage
        st.subheader("Match Percentage")
        st.write(str(round(score, 2)) + "%")

        # Progress bar
        st.progress(int(score))

        st.divider()

        # Missing Skills
        st.subheader("Missing Skills")
        for skill in missing:
            st.error(skill.upper())

        st.divider()

        # Skill Chart
        st.subheader("Skill Match Chart")
        chart = skill_chart(matched, missing)
        st.pyplot(chart)

        st.divider()

        # ATS Score
        st.subheader("ATS Resume Score")

        if score >= 80:
            st.success(f"{round(score)} / 100 - Excellent Match")
        elif score >= 60:
            st.info(f"{round(score)} / 100 - Good Match")
        else:
            st.warning(f"{round(score)} / 100 - Needs Improvement")