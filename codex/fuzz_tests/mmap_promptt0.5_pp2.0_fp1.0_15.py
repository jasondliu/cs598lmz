import mmap
# Test mmap.mmap(fileno, size)
#
# This is just to make sure that the mmap module can be imported.

# Test that the mmap module can be imported.
import mmap
import os
import sys
import unittest
import warnings
from test import support

# Skip test if the platform does not support mmap.
try:
    mmap.mmap(-1, 1)
except (ValueError, EnvironmentError):
    raise unittest.SkipTest("cannot mmap")

# Skip test if the platform cannot open an anonymous mmap.
try:
    mmap.mmap(-1, 1, flags=mmap.MAP_ANON)
except (ValueError, EnvironmentError):
    raise unittest.SkipTest("cannot mmap anonymous")

# Skip test if the platform cannot open an anonymous mmap with
# MAP_SHARED.
try:
    mmap.mmap(-1, 1, flags=mmap.MAP_ANON | mmap.MAP_SHARED)
except (ValueError, EnvironmentError):
    raise unittest.SkipTest("
