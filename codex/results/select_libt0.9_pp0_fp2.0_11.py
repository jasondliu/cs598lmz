import select, sys, threading

CHUNKSIZE = 1024

class Listener(object):
    """
    Wraps a socket we use to listen for connections.
    """

    def __init__(self, address):
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(address)
        self.sock.listen(5)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True


class Client(object):
    """
    Wraps a client connection.
    """

    def __init__(self, sock):
        self.sock = sock
        self.sock.setblocking(0)
        self.sockfile = sock.makefile("rb", 0)
        self.message = ""

    def fileno(self):
        return self.sock.fileno()

    def close(self):
       
