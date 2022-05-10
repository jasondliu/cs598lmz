import io
# Test io.RawIOBase.readinto()
import math
import os
import platform
import random
import select
import sys
import time
import unittest
import warnings

from test import support
from test.support import caught_warning
from test.support import os_helper
from test.support import TESTFN
from test.support import threading_helper
from test.support.script_helper import assert_python_ok

# Skip these tests if there is no Unix sockets support.
support.requires('unix_sockets')

HOST = support.HOST
HOSTv6 = support.HOSTv6
LINUX_ONLY = unittest.skipUnless(sys.platform.startswith("linux"),
                                 'Linux specific tests')
OSX_ONLY = unittest.skipUnless(sys.platform == 'darwin', 'OS X specific tests')
WINDOWS_ONLY = unittest.skipUnless(sys.platform == 'win32',
                                   'Windows specific tests')

if sys.platform.startswith('linux'):
    SOCKET_PAIR = socket.socketpair
