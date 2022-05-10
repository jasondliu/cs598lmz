import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno

from test import test_support

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # This test is not very good, because it will fail if the
        # machine has no network interfaces at all.  That's why we
        # skip this test if gethostname() fails.
        try:
            socket.gethostname()
        except socket.error:
            self.skipTest("no network")
        # We can't use socket.if_nameindex() because that function
        # is broken on Windows (it returns all-zeroes interface
        # indices).
        if os.name == "nt":
            import ctypes
            MAX_INTERFACE_NAME_LEN = 256
            class SOCKET_ADDRESS(ctypes.Structure):
                _fields_ = [("lpSockaddr", ctypes.c_void_p),
                            ("iSockaddrLength", ctypes.c_int)]
            class
