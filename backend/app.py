from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# Gemini API Key
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Gemini Model
model = genai.GenerativeModel(
    "gemini-1.5-flash-latest"
)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Generate Study Plan API
@app.route("/generate-plan", methods=["POST"])
def generate_plan():

    try:

        data = request.get_json()

        goal = data.get("goal")

        if not goal:
            return jsonify({
                "error": "Goal is required"
            }), 400

        prompt = f"""
        Create a detailed and structured study plan for:

        {goal}

        Give:
        - Daily schedule
        - Topics to learn
        - Practice tasks
        - Revision strategy
        - Tips
        """

        response = model.generate_content(prompt)

        plan = response.text

        return jsonify({
            "plan": plan
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)