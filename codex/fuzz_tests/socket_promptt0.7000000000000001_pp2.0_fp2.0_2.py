import socket
# Test socket.if_indextoname(int)

import unittest
from test.support import run_unittest

class If_indextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertTrue(isinstance(socket.if_indextoname(1), str))
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)

if __name__ == '__main__':
    run_unittest(If_indextonameTest)
