import socket
# Test socket.if_indextoname()
import sys
import time
import unittest

from test import support
from test.support import TESTFN, run_unittest, import_module

if not hasattr(socket, 'if_nameindex'):
    raise unittest.SkipTest("if_nameindex not defined")

if not hasattr(socket, 'if_nametoindex'):
    raise unittest.SkipTest("if_nametoindex not defined")

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not defined")

if not hasattr(socket, 'getifaddrs'):
    raise unittest.SkipTest("getifaddrs not defined")

if not hasattr(socket, 'if_nameindex'):
    raise unittest.SkipTest("if_nameindex not defined")

if not hasattr(socket, 'if_nametoindex'):
    raise unittest.SkipTest("if_nametoindex not defined")

