from flask import Flask, render_template, request
from data.roles import generate_roadmap

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-roadmap", methods=["POST"])
def roadmap():

    skills_text = request.form["skills"]

    user_skills = [
        skill.strip()
        for skill in skills_text.split(",")
    ]

    target_role = request.form["role"]

    result = generate_roadmap(
        user_skills,
        target_role
    )

    return render_template(
        "result.html",
        missing_skills=result["missing_skills"],
        projects=result["projects"]
    )

if __name__ == "__main__":
    app.run(debug=True)