import socket
# Test socket.if_indextoname in the normal case.
import test.support, test.support.threading_helper as threading_helper
try:
    socket.if_indextoname(socket.if_nametoindex("lo"))
except OSError as e:
    if e.errno != socket.error:
        raise
else:


    class NetworkConnectionNoServer(threading_helper.ServerThread):

        def __init__(self, server_address):
            super().__init__(server_address)
            self.data = b'We are the knights who say ni!'
            self.sock = None

        def test_client(self):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.server_address)
            self.sock.sendall(self.data)
            received = self.sock.recv(len(self.data))
            self.sock.close()
            self.assertEqual(received, self.data)
            super().tear
