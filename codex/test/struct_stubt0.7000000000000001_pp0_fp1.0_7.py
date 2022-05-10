from _struct import Struct
s = Struct.__new__(Struct)
s.size = 2
s.format = 'hh'
s.endian = '<'
s.pack = lambda buf, offset, values: s.pack_into(buf, offset, *values)
s.unpack = lambda buf, offset: s.unpack_from(buf, offset)[0]

#: Struct to pack/unpack a single 32-bit signed integer
s32 = Struct.__new__(Struct)
s32.size = 4
s32.format = 'i'
s32.endian = '<'
s32.pack = lambda buf, offset, value: s32.pack_into(buf, offset, value)
s32.unpack = lambda buf, offset: s32.unpack_from(buf, offset)[0]

#: Struct to pack/unpack a single 32-bit unsigned integer
u32 = Struct.__new__(Struct)
u32.size = 4
u32.format = 'I'
u32.endian = '<'
