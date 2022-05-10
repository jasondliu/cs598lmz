import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError as e:
        if e.errno == errno.EINVAL:
            print("SKIP")
            raise unittest.SkipTest("if_indextoname() not supported")
        raise

class TestIfIndextoname(unittest.TestCase):

    def test_if_indextoname(self):
        test_if_indextoname()
        self.assertEqual(socket.if_indextoname(1), 'lo')
        self.assertEqual(socket.if_indextoname(2), 'eth0')
        self.assertEqual(socket.if_indextoname(3), 'wlan0')

    def test_if_indextoname_invalid(self):
        test_if_indextoname()
        self.assertRaises(OSError, socket.if_indextoname, 0)
