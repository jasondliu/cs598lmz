import mmap
# Test mmap.mmap()
#
# This test is based on the test_mmap.py test from the Python standard
# library.

import os
import unittest
import mmap
import tempfile
import array
import struct
import sys
import io

from test import support

# Skip this test if the system has no mmap support.
try:
    mmap.mmap(-1, 1)
except EnvironmentError:
    raise unittest.SkipTest("cannot mmap")

# Skip this test if the system has no large file support.
if sys.maxsize <= 2**32:
    raise unittest.SkipTest("cannot mmap large files")

# Skip this test if the system has no 64-bit mmap support.
try:
    mmap.mmap(-1, 1, access=mmap.ACCESS_WRITE, offset=2**63)
except ValueError:
    raise unittest.SkipTest("cannot mmap 64-bit files")

# Skip this test if the system has no 64-bit mmap support.
try:
    mmap.mm
