import socket
# Test socket.if_indextoname()
#
# If a network interface with the given index exists,
# returns the name of the interface.
#
# If the network interface with the given index does not exist,
# returns the string 'unknown'.

import os, sys
import unittest
from test.support import run_unittest, import_module
import_module('_socket')

class IfIndexToNameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # Test that an existing index returns the name of the interface.
        if_name = socket.if_indextoname(1)
        self.assertEqual(if_name, 'lo')

    def test_if_indextoname_unknown(self):
        # Test that an unknown index returns 'unknown'.
        if_name = socket.if_indextoname(999999)
        self.assertEqual(if_name, 'unknown')

def test_main():
    run_unittest(IfIndexToNameTestCase)

if __name__ == '__main__':
