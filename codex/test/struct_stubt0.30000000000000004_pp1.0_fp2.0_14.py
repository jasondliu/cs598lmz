from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

import struct
struct.calcsize('I 2s f')

fmt = '<3s 3s HH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
bytes(header)

struct.unpack(fmt, header)
del header
del img

struct.pack(fmt, b'GIF', b'89a', 256, 256)

for chunk in chunks:
    print(struct.unpack('<L', chunk[:4])[0])
    print(struct.unpack('<L', chunk[-4:])[0])

# struct.pack('>L', 154)
# struct.pack('<L', 154)

# struct.unpack('>L', b'\x00\x9a\x00\x00')
# struct.unpack('<L', b'\x00\x9a\x00\x00')

# struct.
