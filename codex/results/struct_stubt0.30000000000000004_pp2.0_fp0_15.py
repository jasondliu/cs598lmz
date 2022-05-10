from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import time
t = time.localtime()
t

s.pack(*t)

octets = s.pack(*t)
octets

s.unpack(octets)

s.unpack_from(octets, 4)

s = Struct('i?f')
s.unpack_from(octets, 4)

s = Struct('i?f')
s.unpack_from(octets, 4)

s = Struct('i?f')
s.unpack_from(octets, 4)

s = Struct('i?f')
s.unpack_from(octets, 4)

s = Struct('i?f')
s.unpack_from(octets, 4)

s = Struct('i?f')
s.unpack_from(octets, 4)

s = Struct('i?f')
s.unpack_from(octets, 4)

s = Struct
