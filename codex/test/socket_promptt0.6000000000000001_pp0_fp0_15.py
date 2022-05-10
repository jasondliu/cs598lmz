import socket
# Test socket.if_indextoname()
#
# Test socket.if_indextoname() with invalid index
#
# This test is skipped if the system does not have any interfaces.

import unittest
import os
import sys
import errno
import platform
import getpass
import subprocess
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname() not defined")

if not hasattr(socket, 'getifaddrs'):
    raise unittest.SkipTest("getifaddrs() not defined")

if getpass.getuser() != 'root':
    raise unittest.SkipTest("not running as root")

if sys.platform.startswith('win'):
    raise unittest.SkipTest("if_indextoname() not defined on Windows")

