import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support
from socket import *

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        ifname = if_indextoname(1)
        self.assertTrue(ifname)
        self.assertTrue(isinstance(ifname, str))

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
