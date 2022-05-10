import socket
import sys
import time
import json
import threading
import uuid

class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.id = str(uuid.uuid4())
        self.recv_thread = threading.Thread(target=self.recv)
        self.recv_thread.start()

    def send(self, message):
        self.sock.send(message)

    def recv(self):
        while True:
            data = self.sock.recv(1024)
            if data:
                try:
                    data = json.loads(data)
                except:
                    pass
                if data['type'] == 'message':
                    print data['message']
                elif data['type'] == 'id':
                    print data['message']
                elif data['
