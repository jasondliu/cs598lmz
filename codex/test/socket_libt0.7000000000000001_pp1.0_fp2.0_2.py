import socket
from threading import Thread

from flask import Flask, render_template

from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

thread = None

@sockets.route('/echo')
def echo_socket(ws):
	while not ws.closed:
		message = ws.receive()
		ws.send(message)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	if not thread:
		thread = Thread(target=lambda: app.run(port=8080))
		thread.daemon = True
		thread.start()
	app.run(port=8081)
