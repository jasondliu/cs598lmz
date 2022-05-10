import selectors
import socket
import sys
import traceback

__all__ = ['Connection']


class Connection(object):
    def __init__(self, host, port, message_queue):
        self.host = host
        self.port = port
        self.message_queue = message_queue
        self.sel = selectors.DefaultSelector()
        self.messages = []

    def _read(self, conn, mask):
        data = conn.recv(1000)  # Should be ready
        if data:
            self.message_queue.put(data.decode())
        else:
            print('closing', conn)
            self.sel.unregister(conn)
            conn.close()

    def _accept(self, sock, mask):
        conn, addr = sock.accept()  # Should be ready
        print('accepted', conn, 'from', addr)
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self._read)

    def _start_connection(self):
        lsock =
