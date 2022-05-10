import selectors
import socket
import types


class Server:
    def __init__(self, port, selector):
        self.selector = selector
        self.port = port

        self.response = b'''HTTP/1.1 200 OK
        Content-Type: text/plain
        Content-Length: 13
        Hello, world!\n'''

    def _accept_wrapped_conn(self, key, mask):
        conn, addr = self.sock.accept()
        print('Accepted connection from {}'.format(addr))
        conn.setblocking(False)
        self.selector.register(conn, selectors.EVENT_READ, self._read)

    def _read(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                data.response += recv_data
            else:
                print('Closing connection to {}'.format(sock.getpeername()))

