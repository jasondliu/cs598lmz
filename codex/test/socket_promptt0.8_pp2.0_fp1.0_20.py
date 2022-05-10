import socket
# Test socket.if_indextoname


class NetworkInterfaces(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, -9999999)

    def test_if_nametoindex(self):
        self.assertRaises(OSError, socket.if_nametoindex, 'blahblahblah')


class NetworkAPI(unittest.TestCase):

    def test_htons(self):
        self.assertEqual(socket.htons(0), 0)
        self.assertEqual(socket.htons(1 << 16 - 1), 1 << 16 - 1)
        if hasattr(socket, 'ntohs'):
            self.assertEqual(socket.htons(socket.ntohs(1 << 16 - 1)), 1 << 16
                - 1)
        self.assertRaises(OverflowError, socket.htons, 1 << 16)
