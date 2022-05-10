import io
# Test io.RawIOBase, io.BufferedIOBase, and io.TextIOBase

import unittest
from unittest import mock
import io
import os
import sys
import time
import gc
import selectors

# This test may deadlock if run under certain debuggers
# (e.g. WinPDB when used with Python 3.2+).  One known way to provoke this
# is to run this test normally and set a breakpoint in
# RawIOBase.readinto().
# On Windows, the issue is that the PDB file lock mechanism is *not*
# overridden by the fcntl function, and so blocks.  On Linux, the issue
# seems to be that the pthread_mutex_lock() in _io.cpython-35m-x86_64-linux-gnu.so
# is not overridden, and so blocks.
# The solution is to use a debugger that doesn't lock the file (e.g.
# Winpdb with Python 3.1).
@unittest.skipUnless(sys.platform == "win32",
    "This test is specific to Windows")
