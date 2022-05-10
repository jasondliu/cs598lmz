import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not defined")

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        #
        # This test is not very useful on its own, but it is used by
        # test_if_nameindex to check that the index returned by
        # if_nameindex() is valid.
        #
        # The test is skipped if there are no interfaces on the system.
        #
        # The test is also skipped if the system does not support
        # if_indextoname().
        #
        # The test is also skipped if the system does not support
        # if_nameindex().
        #
        # The test is also skipped if the system does not support
        # if_nametoindex().
        #
        # The test is also skipped if the
