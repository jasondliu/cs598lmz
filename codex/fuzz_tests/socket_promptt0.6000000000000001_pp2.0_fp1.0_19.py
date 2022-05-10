import socket
# Test socket.if_indextoname()
#
# The function should return None if the index is not valid.
#
# On Windows there is no mapping between if_indextoname() and if_nametoindex()
# because the index is not a stable value.
#
# On Linux if_indextoname() should return the name of the interface associated
# with the index.

from test import support
import unittest

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test for valid index - return string
        self.assertIsInstance(socket.if_indextoname(1), str)

    def test_if_indextoname_invalid_index(self):
        # Test for invalid index - return None
        self.assertIsNone(socket.if_indextoname(0))

    def test_if_indextoname_negative_index(self):
        # Test for negative index - return None
        self.assertIsNone(socket.if_indextoname(-1))

def test_main():
