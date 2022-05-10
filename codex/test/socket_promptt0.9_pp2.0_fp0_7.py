import socket
# Test socket.if_indextoname
#
import sys
import unittest
from test.support import requires_unicode
from test.support import run_unittest

requires_unicode('utf-8')

class GetAddressInfoTestCase(unittest.TestCase):

    gai_errors = (socket.EAI_ADDRFAMILY, socket.EAI_AGAIN, socket.EAI_BADFLAGS,
        socket.EAI_FAIL, socket.EAI_FAMILY, socket.EAI_MEMORY, socket.EAI_NODATA,
        socket.EAI_NONAME, socket.EAI_SERVICE, socket.EAI_SOCKTYPE,
        socket.EAI_SYSTEM)

    def setUp(self):
        self.cm = socket.getaddrinfo
        socket.getaddrinfo = self.gaicb

    def tearDown(self):
        socket.getaddrinfo = self.cm

    def gaicb(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

