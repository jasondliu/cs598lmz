import socket
# Test socket.if_indextoname(index)

import unittest
from test.support import run_unittest, verbose

class InterfaceTest(unittest.TestCase):

    def test_if_indextoname(self):
        """Tests socket.if_indextoname(interface_index)"""
        if verbose:
            print("\nTrying socket.if_indextoname ...")
        interface_index = socket.if_nametoindex('lo')
        name = socket.if_indextoname(interface_index)
        self.assertEqual(name, 'lo')

    def test_if_indextoname_invalid_index(self):
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)


def test_main():
    run_unittest(InterfaceTest)


if __name__ == "__main__":
    test_main()
