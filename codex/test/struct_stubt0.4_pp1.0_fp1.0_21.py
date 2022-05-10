from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import struct
struct.calcsize('i?f')

octets = s.pack(1, False, 2.7)
octets

s.unpack(octets)

# The struct module also provides a function, iter_unpack, that returns an iterator 
# producing tuples unpacked from successive chunks of data.

octets = b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?'
list(s.iter_unpack(octets))

# The struct module can also pack and unpack data to and from files.

with open('data.bin', 'wb') as f:
    f.write(octets)

with open('data.bin', 'rb') as f:
    data = f.read()

