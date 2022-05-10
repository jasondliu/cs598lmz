import socket
# Test socket.if_indextoname()

import unittest
from test import support
from test.support import TESTFN

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # This test is not very good, but it's better than nothing.
        # It would be nice if we could test that the name returned
        # by if_indextoname() is a valid interface name, but I don't
        # know how to do that.
        self.assertTrue(socket.if_indextoname(1))

def test_main():
    support.run_unittest(IfIndextonameTestCase)

if __name__ == "__main__":
    test_main()
