import _struct
# Test _struct.Struct.
from _struct import Struct

import unittest
import sys
from test.support import run_unittest, precisionbigmemtest

from test import mapping_tests

from _testcapi import INT_MAX

if sys.byteorder == "little":
    littleendian_ints = (
            (1, b'\x01'),
            (2, b'\x02'),
            (5, b'\x05'),
            (6, b'\x06'),
            (255, b'\xff'),
            (256, b'\x00\x01'),
            (257, b'\x01\x01'),
            (65535, b'\xff\xff'),
            (65536, b'\x00\x00\x01\x00'),
            (65537, b'\x01\x00\x01\x00'),
            (16777215, b'\xff\xff\xff'),
            (16777216, b'\x00\x00\x00\x01\x00'),
            (1677
