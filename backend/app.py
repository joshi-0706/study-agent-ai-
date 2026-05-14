from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# Configure Gemini API
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Gemini Model
model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

# Home Route
@app.route("/")
def home():
    return render_template("index.html")


# Generate Study Plan Route
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

        Include:
        - Day wise schedule
        - Topics
        - Practice problems
        - Revision plan
        - Tips for consistency
        """

        response = model.generate_content(prompt)

        return jsonify({
            "plan": response.text
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)