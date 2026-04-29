from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"answer": "Please type something."})

    response = get_response(user_message)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
