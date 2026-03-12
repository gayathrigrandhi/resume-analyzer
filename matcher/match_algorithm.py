def calculate_match(job_skills, resume_skills):

    job_set = set(job_skills)
    resume_set = set(resume_skills)

    matched_skills = job_set.intersection(resume_set)
    missing_skills = job_set - resume_set

    score = 0

    if len(job_set) > 0:
        score = (len(matched_skills) / len(job_set)) * 100

    return score, list(matched_skills), list(missing_skills)