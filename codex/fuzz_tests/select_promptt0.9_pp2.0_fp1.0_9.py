import select
# Test select.select() on sockets

import socket
import select
import time
import errno

import unittest
from test.support import (run_unittest,
                          reap_children,
                          check_warnings,
                          check_sizeof)
# Skip these tests if there is no support for the desired
# version of the select module
try:
    select.select([], [], [], 1)
except AttributeError:
    raise unittest.SkipTest("select.select() not defined")

NY = len(select.select([], [], [], 1)) # number of select lists

class SockMgr:
    """Helper class for object-oriented socket management."""
    def __init__(self, tc, family, type_):
        self.tc = tc
        self.s = socket.socket(family, type_)
        tc.assertFalse(self.s.closed, "Socket is already closed.")
        self.known_fd = None

    def __getattr__(self, name):
        """Return a wrapper method that asserts the socket hasn't closed."""
