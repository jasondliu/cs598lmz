import mmap
# Test mmap.mmap(0, 1) on Windows.  If this fails (and it will on Windows
# 7), an exception is raised and the test skipped.
try:
    mmap.mmap(0, 1)
except:
    raise SkipTest('mmap.mmap(0, 1) failed')

from support import _4G, _4Gplus1, BigmemTestCase, unlink, get_attribute
import os
import sys
import gc
import shutil
import tempfile
import unittest

from test import test_support

try:
    import ctypes
except ImportError:
    ctypes = None


class MmapTests(BigmemTestCase):
    # How big to make the test file in bytes
    filesize = 1024 * 1024

    # The number of times to repeat the test in each run
    repeat = 5

    # This is a class variable so that it can be overridden in subclasses
    # without modifying the class object in the superclass.
    filename = test_support.TESTFN
