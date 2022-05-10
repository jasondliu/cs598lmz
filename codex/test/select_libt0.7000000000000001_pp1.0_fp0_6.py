import select
import socket
import threading
import time


class Listener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.data = None

        self.sock = socket.socket()
        self.sock.bind(("", port))
        self.sock.listen(1)

        self.running = True
        self.start()

    def stop(self):
        self.running = False
        self.join()

