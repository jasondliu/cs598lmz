import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")

class Server(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", 8080))
        self.sock.listen(5)
        self.threads = []
        self.lock = threading.Lock()

    def run(self):
        while True:
            client, address = self.sock.accept()
            print("Accepted connection from %s:%d" % (address[0], address[1]))
            t = threading.Thread(target=self.handle, args=(client, address))
            t.start()
            self.threads.append(t)

    def handle(self, client, address):
        while True:
            data = client.recv(1024)
            if not data:
                break

