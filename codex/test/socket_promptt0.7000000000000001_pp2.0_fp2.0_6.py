import socket
# Test socket.if_indextoname()

from test_socket import test_support
if not hasattr(socket, "if_indextoname"):
    raise test_support.TestSkipped("interface lookup not available")


import socket
import os
import struct
import sys
import unittest


try:
    socket.if_indextoname(1)
except socket.error as err:
    if err.errno == socket.errno.ENXIO:
        raise test_support.TestSkipped("No interfaces found")
    else:
        raise


class InterfaceTest(unittest.TestCase):

    def test_basic(self):
        try:
            for i in range(100):
                name = socket.if_indextoname(i)
                if name:
                    idx = socket.if_nametoindex(name)
                    self.assertEqual(i, idx)
        except socket.error as msg:
            # skip not-found errors
            if msg.errno != socket.errno.ENXIO:
                raise


