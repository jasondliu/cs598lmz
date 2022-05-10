import socket
# Test socket.if_indextoname()

import os, sys
import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        ifname = socket.if_indextoname(1)
        self.assertTrue(ifname is not None)
        self.assertTrue(ifname != "")

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
