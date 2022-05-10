import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not available")

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        #
        # This test is not very good, but it's better than nothing.
        #
        # XXX: This test should be improved.
        #
        # XXX: This test should be moved to a more appropriate place.
        #
        # XXX: This test should be extended to test if_indextoname()
        #      with invalid arguments.
        #
        # XXX: This test should be extended to test if_indextoname()
        #      with valid arguments.
        #
        # XXX: This test should be extended to test if_indextoname()
        #      with valid arguments that are not interfaces.
        #
        # XXX: This test should
