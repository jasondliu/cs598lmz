import socket
import threading
import time
import json

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.connect((host, port))
        self.sock.setblocking(False)

        self.read_thread = threading.Thread(target=self.read_loop)
        self.read_thread.start()

        self.write_thread = threading.Thread(target=self.write_loop)
        self.write_thread.start()

    def read_loop(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    data = json.loads(data)
                    print(data)
                else:
                    break
            except:
                pass

    def write_loop(self):
        while True:
            try:
                msg = input()
                msg = json.dumps(msg)
                self.sock.send(msg)
            except:
                pass

