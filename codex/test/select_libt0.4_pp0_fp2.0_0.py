import select

from . import client

class SelectClient(client.Client):
    def __init__(self, host, port, timeout=None):
        super().__init__(host, port, timeout)
        self.sock.setblocking(False)

    def _read(self, max_size):
        # select.select() is used to wait until the socket is ready to read.
        # Note that select() is a blocking call, even though the socket is
        # non-blocking.
        r, w, e = select.select([self.sock], [], [], self.timeout)
