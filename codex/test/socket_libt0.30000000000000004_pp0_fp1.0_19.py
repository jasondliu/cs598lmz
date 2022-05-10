import socket
import threading
import time

from util import *

class Server:
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('0.0.0.0', port))
        self.sock.listen(5)
        self.connections = []
        self.connections_lock = threading.Lock()
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        while self.running:
            connection, address = self.sock.accept()
            self.connections_lock.acquire()
            self.connections.append(connection)
            self.connections_lock.release()

    def stop(self):
        self.running = False

