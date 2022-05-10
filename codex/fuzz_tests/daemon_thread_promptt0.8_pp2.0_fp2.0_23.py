import threading
# Test threading daemon
# source: https://stackoverflow.com/questions/21409941/how-to-kill-all-threads-when-main-thread-exits-in-python-3-3

class MyDaemon(threading.Thread):
    def run(self):
        print("Hello from a thread")
        for n in range(1,1000000):
            print(n)

for n in range(1,5):
    t = MyDaemon()
    print("Starting a thread")
    t.setDaemon(True)
    t.start()
    print("Thread started")

print("Exiting Main Thread")

# if __name__ == '__main__':
#     testThreads()

# Test flask_socketio
from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg
