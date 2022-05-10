from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(_, 0)

s.unpack_from(_, 0)

s.unpack_from(_, 4)

s = Struct('iif')
s.size

s.pack(1, 2, 3.0)

s.unpack(_)

s.unpack_from(_, 0)

s.unpack_from(_, 4)

s.unpack_from(_, 8)

s = Struct('iif')
s.size

s.pack(1, 2, 3.0)

s.unpack(_)

s.unpack_from(_, 0)

s.unpack_from(_, 4)

s.unpack_from(_, 8)

s = Struct('iif')
s.size

s.pack(1, 2, 3.0)

s.unpack(_)

s.unpack_from(_, 0)

