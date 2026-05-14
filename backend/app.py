from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate-plan", methods=["POST"])
def generate_plan():

    data = request.json
    goal = data["goal"]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a study planner AI."
            },
            {
                "role": "user",
                "content": f"Create a study plan for: {goal}"
            }
        ]
    )

    plan = response.choices[0].message.content

    return jsonify({
        "plan": plan
    })


if __name__ == "__main__":
    app.run(debug=True)