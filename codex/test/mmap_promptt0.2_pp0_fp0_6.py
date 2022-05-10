import mmap
# Test mmap.mmap()
#
# This test is based on the test_mmap.py test in the Python test suite.
#
# The test_mmap.py test is Copyright (c) 2001, 2002 Python Software
# Foundation; All Rights Reserved.  See the file PSF-LICENSE for details.

import os
import sys
import unittest
import mmap
import array
import struct
import tempfile
import time
import warnings

from test import test_support

# Skip this test if the OS doesn't support anonymous mmap's.
try:
    mmap.mmap(-1, 1)
except (EnvironmentError, ValueError):
    raise unittest.SkipTest("anonymous mmap not supported")

# Skip this test if the OS doesn't support large file offsets.
try:
    mmap.mmap(-1, 1, offset=2**31)
except (EnvironmentError, ValueError):
    raise unittest.SkipTest("large file offsets not supported")

# Skip this test if the OS doesn't support file-backed mmap's.
