import mmap
# Test mmap.mmap()
#
# This test is derived from the test case for mmap.mmap() in the Python
# standard library.
#
# The test case is a bit too long, so it is split into two parts.
#
# This file contains the first part.
#
# The second part is in test_mmap_mmap2.py.

import os
import sys
import unittest
import mmap
import struct
import tempfile
import array

from test import support

# Skip this test if the system does not have a /dev/zero.
if not hasattr(os, 'O_RDWR'):
    raise unittest.SkipTest("requires os.O_RDWR")

try:
    fd = os.open('/dev/zero', os.O_RDWR)
except OSError:
    raise unittest.SkipTest("requires /dev/zero")
else:
    os.close(fd)

# Skip this test if the system does not have a /dev/full.
try:
    fd = os.open('/dev/
