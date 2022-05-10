from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# <codecell>

s.pack(1, 'ab', 2.7)

# <codecell>

s.unpack(_)

# <codecell>

s.unpack(s.pack(1, 'ab', 2.7))

# <codecell>

s = Struct('I 2s f')
s.pack(1, 'ab', 2.7)

# <codecell>

s.unpack(_)

# <codecell>

s.unpack(s.pack(1, 'ab', 2.7))

# <codecell>

import struct
struct.pack('>I', 10240099)

# <codecell>

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# <codecell>

for c in b'\xf0\xf0\xf0\xf0\x80\x80':
    print(c)
