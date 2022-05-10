import io
# Test io.RawIOBase

import _io
import os
import sys
import unittest
from test.support import TESTFN, run_unittest, import_module

# Skip tests if _io wasn't compiled with unicode support
try:
    _io.open("\xe9", "w")
except UnicodeError:
    raise unittest.SkipTest("io.open does not support unicode filenames")

# Skip tests if the OS doesn't support file descriptor passing.
try:
    os.pipe()
except OSError:
    raise unittest.SkipTest("os.pipe() failed")

# Skip tests if the OS doesn't support non-blocking I/O on pipes.
try:
    import fcntl
except ImportError:
    raise unittest.SkipTest("fcntl module not found")
else:
    try:
        fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
    except IOError:
        raise unittest.SkipTest("fcntl module doesn't support "
                               
