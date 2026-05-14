from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

        # Sample AI Study Plan
        sample_plan = f"""
📚 STUDY PLAN FOR: {goal}

━━━━━━━━━━━━━━━━━━━━━━

📅 Day 1-2
• Learn Arrays
• Time Complexity Basics
• Solve 5 Array Problems

📅 Day 3-4
• Learn Strings
• String Manipulation
• Practice Pattern Problems

📅 Day 5-6
• Linked Lists
• Insertion & Deletion
• Reverse Linked List Problems

📅 Day 7-8
• Stacks and Queues
• Implement Stack using Array
• Solve Queue Problems

📅 Day 9-10
• Recursion Basics
• Recursive Problem Solving

📅 Day 11-13
• Trees and Binary Trees
• Traversals
• Binary Search Tree Basics

📅 Day 14-15
• Graph Basics
• BFS and DFS

📅 Day 16-17
• Dynamic Programming
• Fibonacci
• Knapsack Problems

📅 Day 18
• Revision Day
• Revisit Weak Topics

📅 Day 19
• Mock Coding Interview
• Solve Timed Problems

📅 Day 20
• Final Revision
• HR + Technical Interview Prep

━━━━━━━━━━━━━━━━━━━━━━

✅ DAILY TIPS
• Practice coding every day
• Revise notes before sleeping
• Focus on problem-solving
• Spend at least 2 hours daily
• Maintain consistency

🚀 ALL THE BEST!
"""

        return jsonify({
            "plan": sample_plan
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)