import mmap
# Test mmap.mmap()
#
# This test is derived from the mmap module test suite.
#
# Copyright (c) 2001-2004 Python Software Foundation; All Rights Reserved
#
# Author: Guido van Rossum

import unittest
import os
import mmap
import struct
import sys
import tempfile
import time
import array

from test import test_support

# Some tests fail on Windows if the file is too small.
MIN_LEN = 1024

# Some tests fail on Windows if the file is too large.
MAX_LEN = 1024 * 1024

# Some tests fail on Windows if the file is not aligned on a 512-byte boundary.
ALIGNMENT = 512

# Some tests fail on Windows if the file is not aligned on a 4096-byte boundary.
PAGE_ALIGNMENT = 4096

# Some tests fail on Windows if the file is not aligned on a 65536-byte boundary.
LARGE_ALIGNMENT = 65536

# Some tests fail on Windows if the file is not aligned on a 1048576-byte boundary.
HUGE_ALIGNMENT = 1048576


