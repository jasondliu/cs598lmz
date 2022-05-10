import socket
# Test socket.if_indextoname()

if_indextoname = socket.if_indextoname

class TestSocket(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertRaises(ValueError, if_indextoname, -1)
        self.assertRaises(ValueError, if_indextoname, 0)
        self.assertRaises(ValueError, if_indextoname, 1<<32)
        self.assertRaises(OSError, if_indextoname, 1<<31)
        self.assertRaises(OSError, if_indextoname, 1<<30)
        self.assertRaises(OSError, if_indextoname, 1<<29)
        self.assertRaises(OSError, if_indextoname, 1<<28)
        self.assertRaises(OSError, if_indextoname, 1<<27)
        self.assertRaises(OSError, if_indextoname, 1<<26)
        self.assertRaises(OSError, if_indext
