#Role requirements and roadmap data
ROLES = {
    "AI Engineer": {
        "skills": [
            "Python",
            "SQL",
            "Statistics",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "Git",
            "Data Structures"
        ],
        "projects": [
            "Titanic Survival Prediction",
            "Resume Skill Gap Analyzer",
            "AI Study Assistant",
            "Interview Simulator"
        ]
    },

    "Data Scientist": {
        "skills": [
            "Python",
            "SQL",
            "Statistics",
            "Machine Learning",
            "Pandas",
            "NumPy",
            "Data Visualization"
        ],
        "projects": [
            "Sales Dashboard",
            "Customer Segmentation",
            "Stock Analysis",
            "Data Analytics Platform"
        ]
    },

    "Frontend Developer": {
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git",
            "Responsive Design"
        ],
        "projects": [
            "Portfolio Website",
            "Weather Dashboard",
            "Task Manager",
            "E-Commerce UI"
        ] 
    }
}

def generate_roadmap(user_skills, target_role):
    role_data = ROLES.get(target_role)
    if not role_data:
        return None
    required_skills = role_data["skills"]
    missing_skills = [
        skill for skill in required_skills
        if skill.lower() not in [s.lower() for s in user_skills]
    ]
    return {
        "missing_skills": missing_skills,
        "projects": role_data["projects"]
    }