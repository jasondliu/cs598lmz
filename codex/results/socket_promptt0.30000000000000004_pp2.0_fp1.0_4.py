import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndexToNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # On Windows, this test is not reliable.
        if support.platform == 'win32':
            self.skipTest('Windows does not support this test')

        # Test if_indextoname()
        self.assertEqual(socket.if_indextoname(1), 'lo')

    def test_if_indextoname_invalid_index(self):
        # On Windows, this test is not reliable.
        if support.platform == 'win32':
            self.skipTest('Windows does not support this test')

        # Test if_indextoname() with invalid index
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, -1)

if __name__ == "__main__":
    unittest.main()
