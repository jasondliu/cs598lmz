import socket
# Test socket.if_indextoname
from test import support
import unittest
try:
    socket.if_indextoname(1)
except socket.error:
    raise unittest.SkipTest('if_indextoname not supported')
support.requires('network')


class IfIndexToNameTest(unittest.TestCase):

    @unittest.skipUnless(hasattr(socket, 'if_indextoname'),
        'if_indextoname doesn\'t exist on this platform')
    def test_valid_index(self):
        name = socket.if_indextoname(1)
        self.assertNotEqual(name, None, 'Got name is empty')

    @unittest.skipUnless(hasattr(socket, 'if_indextoname'),
        'if_indextoname doesn\'t exist on this platform')
    def test_invalid_index(self):
        self.assertRaises(OSError, socket.if_indextoname, 9999)


if __name__ == '__main__':
    unittest.main()
