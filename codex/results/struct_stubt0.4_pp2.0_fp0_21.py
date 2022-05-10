from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

# unpack

data = s.pack(1, False, 2.7)
s.unpack(data)

# unpack_from

import sys
offset = 0
record_size = s.size
while True:
    record_data = data[offset:offset + record_size]
    if record_data == b'':
        break
    record = s.unpack(record_data)
    print(record)
    offset += record_size

# pack_into

data = bytearray(b'Hello World')
s.pack_into(data, 0, 1, False, 2.7)
data

# unpack_from

s.unpack_from(data, 0)

# endianness

s = Struct('>i?f')
s.pack(1, False, 2.7)

s = Struct('<i?f')
s.pack(1, False, 2.7)

# alignment

s = Struct('i?f')
