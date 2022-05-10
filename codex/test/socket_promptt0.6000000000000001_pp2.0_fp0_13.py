import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import platform
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        test_if = 'lo'
        if_index = socket.if_nametoindex(test_if)
        if_name = socket.if_indextoname(if_index)
        self.assertEqual(test_if, if_name)

    def test_if_indextoname_error(self):
        self.assertRaises(OSError,
                          socket.if_indextoname,
                          -1)

if __name__ == '__main__':
    unittest.main()
