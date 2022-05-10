import socket
# Test socket.if_indextoname() function

import unittest
import socket

from test import support

def get_test_if_indextoname(families):
    def test_if_indextoname(self):
        # bpo-39986: Check if all known family interfaces are found
        for family in families:
            expected = [name for name, _, _ in socket.if_nameindex()
                        if socket.has_ipv6 and family == socket.AF_INET6 or
                           not socket.has_ipv6 and family == socket.AF_INET or
                           not socket.has_ipv6 and socket.AF_INET6 not in families]
            try:
                with support.check_warnings(quiet=True) as w:
                    index = socket.if_nametoindex(expected[0])
                    actual = socket.if_indextoname(index, family)
            except (OSError, ValueError):
                actual = None
            if actual and expected:
                self.assertIn(actual, expected)
    return test_if_indextoname
