# app.py

from flask import Flask, render_template, request, jsonify
from game_generator import generate_game_code

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    output = generate_game_code(prompt)
    return render_template("index.html", output=output)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    reply = generate_game_code(user_message)
    return jsonify({'reply': reply})

if __name__ == "__main__":
    app.run(debug=True)
