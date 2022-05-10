import ctypes
# Test ctypes.CFields of structures with bitfields in C++ code.
#

from _ctypes import Union, Structure
import unittest

class BitfieldsTestCase(unittest.TestCase):
    def make_obj(self, name, fields, offset_and_sizes):
        obj_fields = []
        offset = 0
        for name, value in fields:
            bit_size = value.bit_length()
            obj_fields.append((name, value))
            offset_and_sizes.append((offset, bit_size))
            offset += bit_size
        obj = type(name, (Structure,), {'_fields_': obj_fields})
        return obj

    def make_u64(self, offset_and_sizes):
        return self.make_obj('U64', [('x', ctypes.c_uint64)], offset_and_sizes)

    def make_u32(self, offset_and_sizes):
        return self.make_obj('U32' , [('x', ctypes.c_uint32)], offset_and_s
