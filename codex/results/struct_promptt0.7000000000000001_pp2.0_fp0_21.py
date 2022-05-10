import _struct
# Test _struct.Struct
import test.support
import unittest

# Expected result for Big- and Little-Endian, Aligned and Packed.
BE_STD = [b'\000\001\002\003\004\005\006\007', b'\001\000', b'\002\000',
          b'\003\000', b'\004\000', b'\005\000', b'\006\000\007\000']
LE_STD = [b'\000\001\002\003\004\005\006\007', b'\000\001', b'\000\002',
          b'\000\003', b'\000\004', b'\000\005', b'\000\006\000\007']

# Expected result for Big- and Little-Endian, Unaligned and Unpacked.
BE_NONSTD = [b'\001\000\002\003\004\005\006\000', b'\001\000', b'\003\000',
             b'\005\000', b'\000\006\000
