import socket
# Test socket.if_indextoname()
# This test is expected to fail on Windows.
import test.support
import unittest

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test simple calls
        self.assertEqual(socket.if_indextoname(1), 'lo')
        self.assertEqual(socket.if_indextoname(1, 0), 'lo')
        self.assertEqual(socket.if_indextoname(1, socket.AF_INET), 'lo')
        self.assertEqual(socket.if_indextoname(1, socket.AF_INET6), 'lo')
        # Test invalid index
        with self.assertRaises(OSError):
            socket.if_indextoname(0)
        with self.assertRaises(OSError):
            socket.if_indextoname(0, 0)
        with self.assertRaises(OSError):
            socket.if_indextoname(0, socket.AF_INET)

