from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('ci')
s.size

s.pack(1,'h')
s.unpack(_)
s.unpack_from(b'\x01\x00\x68\x00',1)

s = Struct('hhl')
s.unpack(b'\x01\x02\x00\x00\x00\x03\x00\x00\x00\x04')

s = Struct('hhl')
s.pack(1,2,3)
s.pack_into(buffer,0,1,2,3)

s = Struct('hhl')
s.pack_into(b'\x00'*12,0,1,2,3)


import struct
struct.pack('>I',10240099)

struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
struct.pack('>i',-1)
struct.calcsize('>i')

struct.pack('>I',1)
