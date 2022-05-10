import _struct
# Test _struct.Struct.pack_into()
#
# This version uses PyMem_Malloc() to allocate the buffer, instead of the PyMem_Malloc() in
# the original test.

import sys
import sysconfig
import _multiprocessing
import unittest
from test import support

class subTest(unittest.TestCase):
    def check_pack(self, format, bufsize, *values):
        s = _struct.Struct(format)
        buf = _multiprocessing.PyMem_Malloc(bufsize)
        s.pack_into(buf, 0, *values)
        unpacked = s.unpack_from(buf, 0)
        self.assertEqual(unpacked, values)
        _multiprocessing.PyMem_Free(buf)

    def test_byte_order(self):
        # Issue #8060: native byte order should be used by default
        if sys.byteorder == 'little':
            self.check_pack('@H', 2, 0x0100)
            self.check_pack('=H', 2, 0x
