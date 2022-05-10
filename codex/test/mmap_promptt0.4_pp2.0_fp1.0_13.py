import mmap
# Test mmap.mmap.resize()
import os
import platform
import struct
import tempfile
import unittest
from test import support
from test.support import bigmemtest

try:
    import mmap
except ImportError:
    raise unittest.SkipTest("mmap module not available")

if (sys.platform.startswith('aix') or sys.platform.startswith('freebsd') or
    sys.platform.startswith('openbsd') or sys.platform.startswith('netbsd') or
    sys.platform.startswith('osf1') or sys.platform.startswith('sunos')):
    raise unittest.SkipTest("mmap.resize() not available on this platform")

if sys.platform == 'darwin' and sys.maxsize > 2**32:
    raise unittest.SkipTest("mmap.resize() not available on this platform")

if sys.platform == 'win32':
    import msvcrt

PAGESIZE = mmap.PAGESIZE

# This is the minimum size of a
