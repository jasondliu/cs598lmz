import select
# Test select.select()
#
# This test is designed to detect a bug in the select() function
# that caused it to return incorrect results for large file
# descriptors.  This bug is present in Python 2.3.3 but not in
# Python 2.3.4.

import os
import select
import socket
import sys
import time
import unittest

from test import test_support

# create a socket pair for use in the test
sock_r, sock_w = socket.socketpair()

class SelectTestCase(unittest.TestCase):
    def setUp(self):
        self.old_mask = os.umask(077)

    def tearDown(self):
        os.umask(self.old_mask)

    def test_select(self):
        # Create a temporary file
        test_file_fd = os.open(test_support.TESTFN,
                               os.O_CREAT | os.O_WRONLY | os.O_EXCL)

        # Test select() with the socket and temporary file
        try:
            r,
