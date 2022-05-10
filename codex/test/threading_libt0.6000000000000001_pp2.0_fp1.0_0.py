import threading
threading.Thread(target=lambda: webbrowser.open('http://127.0.0.1:8080')).start()

from flask import Flask, render_template, request
from datetime import datetime

from ai import AI

ai = AI()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ai", methods=["POST"])
def ai():
    data = request.form["data"]
    print("Data received: " + data)
    return ai.respond(data)

app.run(debug=False, port=8080)
