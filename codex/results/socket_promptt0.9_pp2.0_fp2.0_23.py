import socket
# Test socket.if_indextoname() with an invalid argument.
import test.support
import unittest
from test.support.script_helper import assert_python_ok
if_indextoname_helper = test.support.script_helper(
    'if_indextoname_helper.py')


class TestIfIndexToName(unittest.TestCase):

    def test_negative_index(self):
        """Assert that socket.if_indextoname() raises ValueError
        with a negative index."""
        negative_index = -1
        with self.assertRaises(ValueError):
            socket.if_indextoname(negative_index)

    def test_invalid_index(self):
        """Assert that socket.if_indextoname() raises OSError
        with an invalid index (i.e. one which is not mapped to a
        valid interface name)."""
        try:
            with self.assertRaises(OSError):
                unused_interface_name = socket.if_indextoname(test.support.
                    fake_rpi
