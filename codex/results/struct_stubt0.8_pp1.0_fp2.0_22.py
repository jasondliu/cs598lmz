from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__    # doctest: +SKIP
s._fields_    # doctest: +SKIP
s.format      # doctest: +SKIP

s = Struct('x=i,y=f,z=s')    # doctest: +SKIP
s.x           # doctest: +SKIP
s.x = 0       # doctest: +SKIP
s             # doctest: +SKIP
s.size        # doctest: +SKIP
s.format      # doctest: +SKIP
s.pack(3, 6.47, 'abc')     # doctest: +SKIP
s.pack_into(bytearray(s.size), 0, 3, 6.47, 'abc')    # doctest: +SKIP

s.unpack_from(bytearray(s.size), 0)     # doctest: +SKIP

s.unpack(b'\x03\x00\x00\x00\t!\x9a\x99\x99\x99\x99\x99\xf
