import mmap
import os
import socket
import struct
import sys
import tempfile
import threading
import time
import traceback
import types
import unittest

from test import support
from test.support import TESTFN, run_unittest, check_warnings, import_module
from test.support.script_helper import assert_python_ok

import _testcapi

# Tell the test harness we have a third thread running.
threading.current_thread().name = 'MainThread'

HOST = support.HOST

if sys.platform.startswith("win"):
    SOCK_NONBLOCK = socket.SOCK_NONBLOCK
else:
    SOCK_NONBLOCK = os.O_NONBLOCK

# Filename used for testing
if sys.platform.startswith("win"):
    if sys.platform == "win32":
        confname = "test.conf"
    else:
        confname = r"c:\test.conf"
else:
    confname = "/test.conf"

# On OS
