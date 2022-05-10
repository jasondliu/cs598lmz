from _struct import Struct
s = Struct.__new__(Struct)

s.__init__(">HH")

s.pack(65535,0)

s._fmt

s.size

s._len

s._ent

s.__doc__

s.format



s.__str__

str(s)

'Struct(format=">HH")'

s._unpack(b'\xff\xff\x00\x00')

s.unpack(b'\xff\xff\x00\x00')

s.unpack_from(b'\xff\xff\x00\x00',0)

s.unpack_from(b'\xff\xff\x00\x00',2)

s.pack(0,0)

s.pack_into(b'\x00\x00\x00\x00',0,0,0)

s.pack_into(b'\x00\x00\x00\x00',0,65535,0)

