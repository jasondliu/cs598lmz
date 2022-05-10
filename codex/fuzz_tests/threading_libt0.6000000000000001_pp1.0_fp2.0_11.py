import threading
threading.Thread(target=start_server).start()

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

## API for the server
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global board
    global board_lock
    board_lock.acquire()
    board.move(int(request.form['x']), int(request.form['y']), int(request.form['player']))
    board_lock.release()
    return jsonify({'success': True}), 200

@app.route('/state', methods=['GET'])
def state():
    global board
    global board_lock
    board_lock.acquire()
    data = board.get_state()
    board_lock.release()
    return jsonify({'data': data}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.
