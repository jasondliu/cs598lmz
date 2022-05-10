from _struct import Struct
s = Struct.__new__(Struct)
</code>
Note the underscore in <code>_struct</code>. If you type <code>from struct import Struct</code>, you are still importing <code>Struct</code> from <code>_struct</code>, but the name conflicts with <code>struct</code> and you can't access it.
An example
<code>from time import time
from _struct import Struct

# Create the struct unpacker
unpacker = Struct('!I')

# Create the struct packer
packer = Struct('!Q')

t0 = time()
n = 1000000
for i in xrange(n):
    b = packer.pack(12345)
    x = unpacker.unpack(b[4:])[0]
print '1000,000 integers packed and unpacked: %.2f msec per operation' % ((time() - t0) * 1000.0 / n)

from struct import Struct

# Create the struct unpacker
unpacker = Struct('!I')

# Create the struct packer
packer = Struct('!Q')

t0
