import socket
# Test socket.if_indextoname for netlink/linux

class IfindexTest(unittest.TestCase):

    def test_ifindex(self):
        self.assertRaises(socket.error, socket.if_indextoname, -1)
        self.assertRaises(socket.error, socket.if_indextoname, 0x10000)
        self.assertEqual(socket.if_indextoname(0), None)

def test_main():
    support.run_unittest(IfindexTest)

