import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longdouble()
    y = ctypes.c_longdouble()

class fake_zlib:
    def __init__(self):
        self.crc32 = 0

import test.test_support
import unittest

def format_float_or_unknown(x):
    "Format a float or the string '?'."
    if isinstance(x, float):
        return '%.1f' % (x,)
    else:
        return '?'

class FloatTest(unittest.TestCase):
    def test_float(self):
        for num in [1617161771.7650001,
                    math.pi,
                    math.pi**100,
                    math.pi**-100,
                    3.1]:
            write_read(self, num, '<f')
            write_read(self, num, '>f')
            write_read(self, num, '<d')
            write_read(self, num, '>d')
            if has_longdouble:
                write_read(self, num,
