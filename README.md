## Live Demo
https://resume-analyzer-la8orgxi6b3qfj2g3mstxq.streamlit.app/

# Smart ATS Resume Analyzer for Job Matching

## Overview
The Smart ATS Resume Analyzer is a Python-based web application that helps users analyze how well their resume matches a job description.

Many companies use Applicant Tracking Systems (ATS) to filter resumes before recruiters review them. This tool simulates that process by comparing resume skills with job requirements and calculating a match percentage.

## Features
- Upload Resume (PDF or DOCX)
- Automatic Resume Text Extraction
- Skill Detection from Resume
- Job Description Analysis
- Resume vs Job Skill Matching
- Match Percentage Calculation
- Missing Skills Detection
- ATS Resume Score
- Skill Match Visualization

## Tech Stack
Python  
Streamlit  
PyPDF2  
python-docx  
Matplotlib  

## Project Structure
resume-analyzer
│
├── app.py
├── requirements.txt
│
├── assets
├── images
├── matcher
├── nlp_engine
├── parser
├── visualization


## How to Run

Clone the repository

git clone https://github.com/gayathrigrandhi/resume-analyzer.git

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

## Author
Grandhi Gayathri  
B.Tech – Computer Science and Technology  
Sri Vasavi Engineering College

