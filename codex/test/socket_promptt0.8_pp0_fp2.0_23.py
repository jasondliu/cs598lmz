import socket
# Test socket.if_indextoname 
import sys
import unittest
from test import support


class IfIndexNameTests(unittest.TestCase):
    """Test the if_indextoname function."""

    def test_if_indextoname(self):
        """Test the if_indextoname function."""
        if not hasattr(socket, 'if_indextoname'):
            self.skipTest('socket module has no if_indextoname support')

        # If there is no interface with index 1, this will return None.
        self.assertIsNotNone(socket.if_indextoname(1))

        # Test passing an invalid interface index. This will raise a
        # ValueError.
        self.assertRaises(ValueError, socket.if_indextoname, -1)

        # Test passing a string instead of an integer. This will raise a
        # TypeError.
        self.assertRaises(TypeError, socket.if_indextoname, 'a')


