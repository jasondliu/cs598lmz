import select
# Test select.select() with a non-blocking socket.
#
# This test is not very useful on Windows, where select() does not work
# with non-blocking sockets.
import socket
import sys
import time
import unittest
import asyncore
import asynchat
import threading
import errno

from test import test_support

HOST = test_support.HOST

# Some versions of Solaris appear to have problems with select()
# and non-blocking sockets.  If this is true on your system,
# set this to 0.
SELECT_HAS_BROKEN_ERROR_HANDLING = 1

#
# Test the basic behaviour of select()
#

class BasicSelectTestCase(unittest.TestCase):
    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv.setblocking(0)
        self.serv.bind((HOST, 0))
        self.serv.listen(1)
        self.port = self.serv.getsockname()[
