import sys, threading
threading.Thread(target=lambda: robot.start(desired=desired), daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect():
    robot.connect()
    return ""

@app.route('/stop')
def stop():
    robot.stop()
    return ""

@socketio.on('control', namespace='/test')
def test_message(message):
    desired.update({'x' : float(message['dx']), 'y' : float(message['dy']), 'theta' : float(message['dtheta'])})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
