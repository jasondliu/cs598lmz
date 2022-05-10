import socket
# Test socket.if_indextoname()

import os, sys
import unittest
from test import support

if not hasattr(socket, "if_indextoname"):
    raise unittest.SkipTest("if_indextoname not implemented")


class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test socket.if_indextoname()
        # Get all available interfaces
        ifaces = socket.if_nameindex()
        for iface in ifaces:
            # For each interface, get the name
            name = socket.if_indextoname(iface[0])
            # Check that the name is not empty
            self.assertTrue(name)
            # Check that the name is in the list of interfaces
            self.assertIn(name, [i[1] for i in ifaces])


def test_main():
    support.run_unittest(IfIndextoNameTest)


if __name__ == "__main__":
    test_main()
