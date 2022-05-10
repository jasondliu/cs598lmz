from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl')

s.pack(1,2,3)

s.pack_into((), 1, 2, 3)

s.unpack_from((), 0)

s.unpack((), 0)

s.calcsize()

s.format

s.size

s.alignment


s.pack(1, 2, 3, 4)

s.pack_into((), 0, 1, 2, 3, 4)


s.unpack((), 0)

s.unpack_from((), 0)
