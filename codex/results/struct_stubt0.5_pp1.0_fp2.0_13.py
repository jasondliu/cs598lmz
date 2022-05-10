from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
print(s.size)

from _struct import pack
print(pack('>i', 10240099))

from _struct import unpack
print(unpack('>i', b'\x00\x9c@c'))

from _struct import unpack
print(unpack('>i', b'\x00\x9c@c'))

from _struct import pack
print(pack('>i', 10240099))

from _struct import unpack
print(unpack('>i', b'\x00\x9c@c'))
