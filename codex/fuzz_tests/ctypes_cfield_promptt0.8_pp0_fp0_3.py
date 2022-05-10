import ctypes
# Test ctypes.CField() for bitfields.
import unittest
from test import support
import sys

class TestBitFields(unittest.TestCase):

    def test_bitfields(self):
        BITFIELD = ctypes.c_uint32
        class Foo(ctypes.Structure):
            # Define a bitfield which occupies the rightmost
            # 17 bits and the second rightmost 5 bits.
            # 17 bits = 0x1ffff
            # 5 bits = 0x1f
            _fields_ = [('bitfield', BITFIELD, 17),
                        ('bitfield2', BITFIELD, 5)]

        f = Foo()
        f.bitfield2 = 3
        # Set the second bit of bitfield2.
        f.bitfield2 |= 2
        # Clear the first bit of bitfield.
        f.bitfield &= 0xfffe
        # Set the rightmost bit of bitfield
        f.bitfield |= 1
        # Check the first bit of bitfield.
        self.assertEqual(f.bitfield & 1, 1)
        # Check the second bit of bit
