import selectors
import socket
import types


class Client:
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.host = "127.0.0.1"
        self.port = 10001
        self.requests = {}
        self.counter = 0
        self.buffer_size = 16384

    def connect(self):
        self.counter += 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex((self.host, self.port))
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        message = "Hello from client {}".format(self.counter)
        self.requests[sock] = (events, message)
        self.sel.register(sock, events, data=None)

    def service_connection(self):
        for key, mask in self.sel.select(timeout=None):
            sock = key.fileobj
