from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate-plan", methods=["POST"])
def generate_plan():

    try:

        data = request.json
        goal = data["goal"]

        response = model.generate_content(
            f"Create a detailed study plan for: {goal}"
        )

        plan = response.text

        return jsonify({
            "plan": plan
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)