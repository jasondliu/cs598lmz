import socket
# Test socket.if_indextoname() and socket.if_nametoindex()

# The test is skipped if the platform does not support
# socket.if_indextoname() and socket.if_nametoindex()

try:
    socket.if_indextoname
except AttributeError:
    raise unittest.SkipTest('socket.if_indextoname() not supported')
try:
    socket.if_nametoindex
except AttributeError:
    raise unittest.SkipTest('socket.if_nametoindex() not supported')


class IfIndextonameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertIsInstance(socket.if_indextoname(1), str)

    def test_if_nametoindex(self):
        # Test if_nametoindex()
        self.assertIsInstance(socket.if_nametoindex('lo'), int)

