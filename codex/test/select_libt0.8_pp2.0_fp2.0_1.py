import selectors

class UdpMessage:
    def __init__(self, addr, data):
        self.addr = addr
        self.data = data

    def __str__(self):
        return "UdpMessage(%r, %r)" % (self.addr, self.data)

class UdpSocket:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setblocking(False)

    def bind(self, addr):
        self.sock.bind(addr)

    def close(self):
        self.sock.close()

    def sendto(self, addr, data):
        return self.sock.sendto(data, addr)

