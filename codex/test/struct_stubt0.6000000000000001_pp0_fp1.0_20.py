from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s.pack(1)

s.unpack(s.pack(1))

s.unpack_from(s.pack(1),0)

s = Struct('i')

s.pack(1)

s = Struct('>i')

s.pack(1)

s.unpack(s.pack(1))

s.unpack_from(s.pack(1),0)

s.unpack_from(s.pack(1),1)

s.pack_into(s.pack(1),0,1)

s.unpack_from(s.pack(1),1)

s.pack_into(s.pack(1),1,1)

s.unpack_from(s.pack(1),1)

s = Struct('=i')

s.pack(1)

s.unpack(s.pack(1))

s.unpack_from(s.pack(1),0)

s.unpack_
