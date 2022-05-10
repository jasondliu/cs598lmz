import select
# Test select.select() with timeout
#
# If this test hangs, it means that select.select() does not properly
# handle a timeout value of None.
import asyncore
import socket

class TestServer(asyncore.dispatcher):
    def __init__(self):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('', 0))
        self.listen(1)
        self.active = False

    def handle_accept(self):
        self.active = True

class TestClient(asyncore.dispatcher):
    def __init__(self, server):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((server.getsockname()))

    def handle_connect(self):
        self.close()

server = TestServer()
client = TestClient(server)
# We use a
