import mmap
# Test mmap.mmap()
import os
import re
import subprocess
import sys
import time
import threading
import traceback
import unittest
from test import support

# Skip this test if the OS doesn't support mmap.
try:
    mmap.mmap(-1, 1)
except (EnvironmentError, ValueError):
    raise unittest.SkipTest("mmap not available")

if sys.platform == 'darwin' and sys.maxsize > 2**32:
    # Issue #27096: On macOS 10.12, mmap.mmap() crashes in 64-bit mode
    raise unittest.SkipTest("mmap not available on macOS 64-bit")


# Some systems don't have MAP_ANONYMOUS, e.g. OpenBSD.
MAP_ANONYMOUS = getattr(mmap, 'MAP_ANONYMOUS', 0x1000)

# Test cases have to be pickleable, so we can't use a lambda.
