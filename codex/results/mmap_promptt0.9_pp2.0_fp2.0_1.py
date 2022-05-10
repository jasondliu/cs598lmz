import mmap
# Test mmap.mmap() max_len argument
import os
import errno
import unittest
from test import support

def _get_offset(fd):
    offset = mmap.ALLOCATIONGRANULARITY * 2 ** 6
    while True:
        try:
            fd.seek(offset)
            break
        except IOError as err:
            if err.errno != errno.EINVAL:
                raise
            offset >>= 1
    fd.write(b'\0')
    return offset

class MmapMaxLenTests(unittest.TestCase):
    filename = support.TESTFN
    args = 0, mmap.ALLOCATIONGRANULARITY * 2 ** 6
    @classmethod
    def setUpClass(cls):
        with open(cls.filename, 'w+b') as fd:
            fd.write(b'\0' * cls.args[1])
            cls.offset = _get_offset(fd)
        cls.m = mmap.mmap(*cls.args)  # for tests
