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
        # The test is not very reliable, but it's better than nothing.
        #
        # The test is not reliable because it's not possible to know
        # which interfaces are available on the test machine.
        #
        # The test is not reliable because the interface names are not
        # standardized.
        #
        # The test is not reliable because the interface names are not
        # fixed.
        #
        # The test is not reliable because the interface names are
        # different on different platforms.
        #
        # The test is not reliable because the interface names are
        # different on different versions of the same platform.
        #
        # The test is not reliable because
