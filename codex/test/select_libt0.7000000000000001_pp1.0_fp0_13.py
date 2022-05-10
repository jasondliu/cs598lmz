import select
import sys

class Connection:
    def __init__(self, s):
        self.s = s

    def read(self):
        return self.s.recv(1024)

    def write(self, msg):
        self.s.send(msg)

class ClientConnection(Connection):
    def __init__(self, s, addr):
        Connection.__init__(self, s)
        self.addr = addr

    def __str__(self):
        return "%s:%d" % self.addr

    def read(self):
        return self.s.recv(1024)

    def write(self, msg):
        self.s.send(msg)

class ServerConnection(Connection):
    def __init__(self, s):
        Connection.__init__(self, s)

    def __str__(self):
        return "Server"

    def read(self):
        return self.s.recv(1024)

    def write(self, msg):
        self.s.send(msg)

