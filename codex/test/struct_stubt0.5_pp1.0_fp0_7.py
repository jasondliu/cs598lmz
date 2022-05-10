from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size
s.pack(1)
s.unpack(_)
s.unpack_from(_, 0)
s.unpack_from(_, 0, 1)
s.unpack_from(_, 0, 2)
s.iter_unpack(_)
s.iter_unpack(_, 1)
s.iter_unpack(_, 2)
s.format
s.format_char
s.pack_into(_, 0, 1)
s.unpack_from(_, 0)
s.unpack_from(_, 0, 1)
s.unpack_from(_, 0, 2)
s.iter_unpack(_)
s.iter_unpack(_, 1)
s.iter_unpack(_, 2)

# Issue #26180: ensure that Struct.__new__() is a class method
s = Struct('i')
s.__new__(Struct, 'i')
s.__new__(Struct, 'i').format
s.__new__(Struct, 'i').format_char
