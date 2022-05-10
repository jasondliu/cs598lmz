import socket
# Test socket.if_indextoname()
from errno import errorcode

from test import support
from test.support import run_unittest, HAS_IPV6, socket_helper


class If_IndextonameTest(unittest.TestCase):
    def test_error(self):
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 256)

    @support.require_user('root')
    def test_index(self):
        names = socket.if_nameindex()
        for index, name in names:
            self.assertEqual(socket.if_indextoname(index), name)

    @support.require_user('root')
    def test_name(self):
        names = socket.if_nameindex()
        for index, name in names:
            self.assertEqual(socket.if_indextoname(name), name)


