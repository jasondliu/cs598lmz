import socket
# Test socket.if_indextoname()

import os
import sys
import unittest

from test.support import run_unittest, find_unused_port, import_module

# Skip test if there is no if_indextoname()
if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname() not defined")

# Skip test if getnameinfo() does not support NI_NUMERICSERV
getnameinfo = socket.getnameinfo
try:
    getnameinfo(('127.0.0.1', 0), 0)
except socket.gaierror:
    raise unittest.SkipTest("getnameinfo() not supported")
except TypeError:
    # getnameinfo() does not support the flags argument
    def getnameinfo(sockaddr, flags):
        host, port = sockaddr
        return socket.gethostbyaddr(host)[0], str(port)

# Skip test if there is no AF_LINK
