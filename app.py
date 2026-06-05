from flask import Flask, render_template, request, jsonify
from rules import check_rules
from llm import ask_llm

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    clean_input = user_message.lower().strip()

    # Rule Engine
    rule_response = check_rules(clean_input)

    if rule_response:
        response = rule_response

    else:
        response = ask_llm(user_message)

    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)