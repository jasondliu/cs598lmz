import socket
# Test socket.if_indextoname()

# This function is not available on all systems.
try:
    socket.if_indextoname
except AttributeError:
    raise ImportError("socket.if_indextoname not defined")

import unittest
from test import test_support


class IfIndexToNameTest(unittest.TestCase):

    def test_invalid_index(self):
        # invalid index should raise a ValueError
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)


def test_main():
    test_support.run_unittest(IfIndexToNameTest)


if __name__ == "__main__":
    test_main()
