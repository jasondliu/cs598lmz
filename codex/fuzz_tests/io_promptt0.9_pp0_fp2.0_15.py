import io
# Test io.RawIOBase
# (not in 2.7, part of 3.x)

# io.BufferedIOBase may appear in the future but we don't test it
# (requires some changes to the mmap module to support, that's the
#  only reason)

import unittest
from test import test_support as support
from mmap import *
from os import path, fdopen, write, close
from tempfile import TemporaryFile
from struct import pack

class PackReadTest(unittest.TestCase):
    _packing = pack('HHHH', 1, 2, 3, 4)
    _pos = 0

    def read(self, size):
        if self._pos >= len(self._packing):
            return b''
        s = self._packing[self._pos:self._pos+size]
        self._pos += size
        return s

    def tell(self):
        return self._pos

class ReadTest(PackReadTest):
    def read(self, size):
        return self._packing[self._pos:self._pos+size]

class SeekReadTest(PackRead
