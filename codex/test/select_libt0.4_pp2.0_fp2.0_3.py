import selectors
import socket
import types


# A client that just prints incoming data before sending it back
class Client:
    def __init__(self, addr, sel):
        self.addr = addr
        self.in_buffer = b''
        self.out_buffer = b''
        self.sel = sel
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        try:
            self.sock.connect(addr)
        except BlockingIOError:
            pass

        self.events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(self.sock, self.events, data=None)

    def service_connection(self):
        if self.events & selectors.EVENT_READ:
            self.recv()
        if self.events & selectors.EVENT_WRITE:
            self.send()

