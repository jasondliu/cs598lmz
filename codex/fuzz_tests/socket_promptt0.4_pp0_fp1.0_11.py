import socket
# Test socket.if_indextoname()
if_indextoname = socket.if_indextoname
import unittest
from test import support
from test.support import TESTFN

class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertEqual(if_indextoname(0), b'lo')
        self.assertEqual(if_indextoname(1), b'eth0')
        self.assertRaises(OSError, if_indextoname, -1)
        self.assertRaises(OSError, if_indextoname, 100)


def test_main():
    support.run_unittest(IfIndextoNameTest)

if __name__ == '__main__':
    test_main()
