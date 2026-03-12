def extract_skills(text):

    skills_list = [
        "python","java","c","c++","sql","mysql","postgresql",
        "html","css","javascript","react","node","django",
        "flask","machine learning","deep learning","data analysis",
        "pandas","numpy","tensorflow","pytorch","git","github"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills