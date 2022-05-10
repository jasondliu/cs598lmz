import socket
# Test socket.if_indextoname()

from test import test_support

def if_indextoname(index):
    try:
        return socket.if_indextoname(index)
    except OSError as e:
        if e.errno != errno.EINVAL:
            raise
        if not hasattr(errno, "EPROTONOSUPPORT"):
            return ""
        if e.errno != errno.EPROTONOSUPPORT:
            raise

class IF_INDEXTONAME(unittest.TestCase):

    def setUp(self):
        self.if_name  = if_indextoname(1)

    def test_if_indextoname(self):
        self.assertTrue(self.if_name)
        self.assertEqual(if_indextoname(1), self.if_name)
        self.assertEqual(if_indextoname(2), if_indextoname(1))

        self.assertEqual(if_indextoname(-1), None)
