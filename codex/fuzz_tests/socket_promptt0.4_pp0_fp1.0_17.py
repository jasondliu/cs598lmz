import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not defined")

class IfIndextoNameTest(unittest.TestCase):

    def test_basic(self):
        # Test if_indextoname()
        name = socket.if_indextoname(1)
        self.assertIsInstance(name, str)
        self.assertGreater(len(name), 0)

    def test_invalid_index(self):
        # Test if_indextoname() with invalid index
        self.assertRaises(ValueError, socket.if_indextoname, 0)

def test_main():
    support.run_unittest(IfIndextoNameTest)

if __name__ == '__main__':
    test_main()
