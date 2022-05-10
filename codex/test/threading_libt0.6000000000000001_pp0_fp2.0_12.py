import threading
threading.stack_size(67108864)

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_status')
def update_status():
    while True:
        # if True:
        #     return jsonify(status=True)
        # else:
        #     return jsonify(status=False)
        time.sleep(1)
        return jsonify(status=True)

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=80)
    app.run(debug=True)
