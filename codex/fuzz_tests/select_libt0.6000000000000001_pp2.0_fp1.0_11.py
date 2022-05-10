import selectors
import socket
import types

class BaseServer(object):
    def __init__(self, addr, port, handler_class, connections=1):
        self.addr = addr
        self.port = port
        self.handler_class = handler_class
        self.connections = connections
        self.sock = socket.socket()
        self.sock.bind((addr, port))
        self.sock.listen(connections)
        self.sock.setblocking(False)
        self.sel = selectors.DefaultSelector()
        self.sel.register(self.sock, selectors.EVENT_READ, self.accept)

    def accept(self, sock, mask):
        conn, addr = sock.accept()
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.handler_class)

    def run(self):
        try:
            while True:
                events = self.sel.select()
                for key, mask in events:
                    callback = key.data
                    callback
