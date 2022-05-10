from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

calcsize('I 2s f')

import binascii
binascii.hexlify(s.pack(1, 'spam'.encode('utf8'), 3.0))

data = s.pack(1, 'spam'.encode('utf8'), 3.0)
s.unpack(data)

data

data = bytes(data)
data

s.unpack(data)

data = bytearray(data)
data

s.unpack(data)

s = Struct('I 2s f')
s.unpack_from(data)

data

s.unpack_from(data, 4)

data

s = Struct('I 2s f')
s.unpack_from(data, 4)

data

s = Struct('I 2s f')
s.unpack_from(data, 4)

data

s = Struct('I 2s f')
s.unpack_from(data, 4)
