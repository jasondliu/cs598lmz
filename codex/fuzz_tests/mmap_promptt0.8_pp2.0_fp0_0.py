import mmap
# Test mmap.mmap.
#      -tomek
import os.path
import random
import sys
import unittest

import mmap
import test.support
from test import mapping_tests
from test.support import (run_unittest, unlink, BIGGEST_32BIT_FOUND,
                         create_empty_file, verbose)

_PAGESIZE = mmap.PAGESIZE
_4G = (1 << 32)

def _safesize(size):
    if size == 0:
        return 0, False
    size += _PAGESIZE - 1
    return size & -_PAGESIZE, size > _4G

class MmapTests(mapping_tests.BasicTestMappingProtocol):
    kind = mmap.mmap

    def setUp(self):
        fd = os.open(test.support.TESTFN, os.O_CREAT | os.O_RDWR)
        try:
            os.write(fd, b"\0" * _4G)
        finally:
            os.close(fd)
        self
