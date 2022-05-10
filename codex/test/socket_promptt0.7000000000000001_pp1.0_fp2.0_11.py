import socket
# Test socket.if_indextoname by passing an invalid index (65536).

import unittest
from test import support
from socket import AF_INET
from socket import error

class TestInvalidIfIndex(unittest.TestCase):
    def test_invalid_if_index(self):
        self.assertRaises(ValueError, socket.if_indextoname, 65536)

def test_main():
    support.run_unittest(TestInvalidIfIndex)

if __name__ == "__main__":
    test_main()
