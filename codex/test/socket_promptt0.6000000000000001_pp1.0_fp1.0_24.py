import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTestCase(unittest.TestCase):
    def test_if_indextoname(self):
        try:
            socket.if_indextoname(0)
        except OSError:
            pass
        else:
            self.fail("if_indextoname() didn't raise OSError")


def test_main():
    support.run_unittest(IfIndextonameTestCase)

if __name__ == "__main__":
    test_main()
