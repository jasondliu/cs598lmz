import threading
threading.stack_size(2**26)

# Initialize the server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Define the socket
@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

# Run the server
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80, debug=True)
</code>
I have tried changing the port to 8080 and running the server with <code>sudo python server.py</code> but that didn't work either.
I have also tried running <code>sudo ufw allow 80</code> and <code>sudo ufw allow 8080</code> but that also did not work.
I have also tried running <code>sudo iptables -A INPUT -p tcp --dport 80 -
