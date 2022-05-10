import socket
import threading
import time
import json

class Client(threading.Thread):
    def __init__(self, ip, port, queue):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.queue = queue
        self.daemon = True
        self.start()

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        while True:
            self.socket.send(self.queue.get().encode())
            time.sleep(0.1)

    def write(self, data):
        self.queue.put(data)

    def close(self):
        self.socket.close()


class Server(threading.Thread):
    def __init__(self, ip, port, queue):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
