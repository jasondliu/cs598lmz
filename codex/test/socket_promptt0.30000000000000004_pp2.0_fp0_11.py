import socket
# Test socket.if_indextoname()

import sys
import unittest
from test import support
from test.support import os_helper

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not available")

