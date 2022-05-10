import socket
# Test socket.if_indextoname()
# Test socket.if_nametoindex()
# Test socket.if_nameindex()
# Test socket.if_freenameindex()

class IfNameIndexTest(unittest.TestCase):
    def test_if_nameindex(self):
        ifaces = socket.if_nameindex()
        self.assertTrue(ifaces)
        for i in ifaces:
            self.assertTrue(isinstance(i, tuple), i)
            self.assertEqual(len(i), 2)
            self.assertTrue(isinstance(i[0], int), i)
            self.assertTrue(isinstance(i[1], str), i)
        socket.if_freenameindex(ifaces)

    def test_if_indextoname(self):
        ifaces = socket.if_nameindex()
        self.assertTrue(ifaces)
        for i in ifaces:
            self.assertEqual(i[1], socket.if_indextoname(i[0]))
        socket.if_freenameindex(ifaces)
