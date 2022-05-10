import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("socket.if_indextoname not defined")

class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        #
        # This test is not very useful, because it's impossible to know
        # what interface is available on the test machine.  So we just
        # check if the function returns a string.

        name = socket.if_indextoname(1)
        self.assertTrue(isinstance(name, str))

def test_main():
    support.run_unittest(IfIndextoNameTest)

if __name__ == "__main__":
    test_main()
