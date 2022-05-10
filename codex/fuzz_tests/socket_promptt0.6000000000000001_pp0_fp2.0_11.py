import socket
# Test socket.if_indextoname(if_index)

import test.support
import unittest

class IfIndexToNameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # There is at least the loopback interface.
        self.assertIsNotNone(socket.if_indextoname(1))

class IfNameToIndexTest(unittest.TestCase):
    def test_if_nametoindex(self):
        # There is at least the loopback interface.
        self.assertIsNotNone(socket.if_nametoindex('lo'))

class IfNameToIndexErrorsTest(unittest.TestCase):
    def test_if_nametoindex_errors(self):
        self.assertRaises(OSError, socket.if_nametoindex, "")
        self.assertRaises(OSError, socket.if_nametoindex, "a" * 256)

if __name__ == "__main__":
    unittest.main()
