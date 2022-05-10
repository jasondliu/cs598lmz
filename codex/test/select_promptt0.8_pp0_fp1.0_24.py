import select
# Test select.select

class Socket(object):
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.sock.setblocking(0)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.address_family = self.sock.family
        self.socket_type = self.sock.type
        self.protocol_type = self.sock.proto
        self.close_requested = False
        self.closed = False
        self.listening = False
        self.listen_backlog = 0
        self.readable = False
        self.writable = False
        self.accepting = False
        self.do_write = False

    def shutdown(self, how):
        self.sock.shutdown(how)

    def close(self):
        self.s
