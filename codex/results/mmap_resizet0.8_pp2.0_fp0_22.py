import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This prints <code>a</code> as <code>b''</code>.
As per the documentation, <code>m</code> is still open, so the behavior is as expected.
I am wondering if there is any way to fix this (short of copying <code>m</code> to a new memory map)?


A:

<code>import mmap
import struct

with open('test', 'wb') as f:
    f.write(b'\x00')

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(b'\xFF')
    m.seek(0)
    a = m.read_byte()
    print(a)
</code>
Output:
<code>255
</code>

