import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support
from test.support import import_module

if_indextoname = support.import_module('socket').if_indextoname

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        if_indextoname(1)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
