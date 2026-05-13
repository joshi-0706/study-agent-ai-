from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import mysql.connector

app = Flask(__name__)
CORS(app)

# OpenAI API Key
client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY"
)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Joshi@123",
    database="smartstudy"
)

cursor = db.cursor()

@app.route('/generate-plan', methods=['POST'])
def generate_plan():

    data = request.json
    goal = data['goal']

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

    # Save to MySQL
    sql = """
    INSERT INTO tasks (goal, study_plan)
    VALUES (%s, %s)
    """

    values = (goal, plan)

    cursor.execute(sql, values)
    db.commit()

    return jsonify({
        "study_plan": plan
    })

if __name__ == '__main__':
    app.run(debug=True)