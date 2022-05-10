import mmap
# Test mmap.mmap(-1,size) on win
import os
# Test bytearray(str,encoding='utf8') on win
# Test _winapi._FileHandle.write_file
import unittest

from . import utils
from .test_multiprocessing import mp_test_data
from .test_asyncio import (
    run_until_complete, check_bind_socket_error, check_dual_stack)
from .exceptions import ResourceWarning

from test import support

# Regardless of the platform, tests will not run if the local
# machine does not support IPv6. An empty socket.has_ipv6 struct
# is used to disable socket.has_ipv6.
HAVE_LOCAL_IPV6 = socket.has_ipv6
socket.has_ipv6 = True


class SocketTCPTest(unittest.TestCase):

    def testBasicTCPServer(self):
        with support.transient_internet('self.serv_addr[3]'):
            serv = socket.socket(socket.AF_INET, socket.S
