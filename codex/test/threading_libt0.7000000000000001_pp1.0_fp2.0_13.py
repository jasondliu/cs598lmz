import threading
threading.stack_size(67108864)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test',methods = ['GET'])
def test():
    data = request.args.get('data')
    print(data)
    return "OK"

def send_lstm_data(data):
    print('send_lstm_data...')
    print(data)

def send_wavenet_data(data):
    print('send_wavenet_data...')

def send_speech_data(data):
    print('send_speech_data...')
    send_lstm_data(data)
    send_wavenet_data(data)

@app.route('/speech',methods = ['GET'])
def speech():
    data = request.args.get('data')
    print(data)
    send_speech_data(data)

    return "OK"

