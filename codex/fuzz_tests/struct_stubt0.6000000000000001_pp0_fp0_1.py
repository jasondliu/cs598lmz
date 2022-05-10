from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I', '<')
s.unpack(b'\x00\x00\x00\x01')

# test import
import _struct

# test name mangling
import struct
_struct.Struct.__new__(_struct.Struct).__init__('I', '<').unpack(b'\x00\x00\x00\x01')
struct.Struct.__new__(struct.Struct).__init__('I', '<').unpack(b'\x00\x00\x00\x01')
