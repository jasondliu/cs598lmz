import mmap
# Test mmap.mmap.read_byte
# Test mmap.mmap.readline
# Test mmap.mmap.readlines
# Test mmap.mmap.rfind
# Test mmap.mmap.seek
# Test mmap.mmap.size
# Test mmap.mmap.tell
# Test mmap.mmap.write_byte
# Test mmap.mmap.write
# Test mmap.mmap.writelines
# Test mmap.mmap.__getitem__
# Test mmap.mmap.__iter__
# Test mmap.mmap.__len__
# Test mmap.mmap.__setitem__

import mmap
import os
import unittest

from test import support

filename = support.TESTFN

def _check_method(self, methodname, size):
    # Test that the given method works for a small and large file.
    method = getattr(self.m, methodname)
    self.m.seek(0)
    method()
    self.m.seek(0)
    method(size // 2)
