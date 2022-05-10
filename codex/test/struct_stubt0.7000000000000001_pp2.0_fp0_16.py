from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size
s.pack(1)
s.unpack(s.pack(1))[0]
s.unpack_from(b'\x00\x00\x00\x01')
s.unpack_from(b'\x00\x00\x00\x01', 2)

from _struct import calcsize
calcsize('>I')
calcsize('>I2s')

from _struct import pack, unpack, pack_into, unpack_from
pack('>I', 1)
unpack('>I', b'\x00\x00\x00\x01')[0]
bytearray(10)
pack_into('>I', buf, 4, 1)
unpack_from('>I', buf, 4)

from _struct import error
try:
    pack('>I', '1')
except error:
    pass
try:
    pack_into('>I', buf, 4, '1')
except error:
    pass

