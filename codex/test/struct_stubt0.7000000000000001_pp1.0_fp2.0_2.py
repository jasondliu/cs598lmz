from _struct import Struct
s = Struct.__new__(Struct)
s.fmt = '<I'
s.size = 4
s.unpack('\x12\x34\x56\x78')

import _struct
_struct.unpack('<I', '\x12\x34\x56\x78')
