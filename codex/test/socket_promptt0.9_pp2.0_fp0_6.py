import socket
# Test socket.if_indextoname - if_indexname(index) -> if_name

import socket
import unittest
from test import support

class IfIndextoNameTest(unittest.TestCase):
    def test_if_indextoname(self):
        if_index = socket.if_nametoindex('lo0')
        self.assertTrue(if_index > -1)
        self.assertEqual('lo0', socket.if_indextoname(if_index))
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)


def test_main():
    support.run_unittest(IfIndextoNameTest)

if __name__ == "__main__":
    test_main()
