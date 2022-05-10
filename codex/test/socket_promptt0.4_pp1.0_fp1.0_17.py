import socket
# Test socket.if_indextoname

import os
import sys
import unittest
from test import support
from socket import if_indextoname

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        if_indextoname(0)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
