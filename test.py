from data.roles import generate_roadmap
user_skills = [
    "Python", 
    "HTML", 
    "CSS"
]
result = generate_roadmap(
    user_skills, 
    "AI Engineer"
)
print(result)