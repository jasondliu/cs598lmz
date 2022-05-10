import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # All interfaces should have a name
        for i in range(256):
            try:
                name = socket.if_indextoname(i)
            except OSError:
                pass
            else:
                self.assertTrue(name)
                self.assertEqual(socket.if_nametoindex(name), i)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
