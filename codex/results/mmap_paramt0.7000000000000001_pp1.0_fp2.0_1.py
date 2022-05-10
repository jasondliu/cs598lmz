import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[:] = b'\x02'
</code>
However, this only writes the byte <code>0x02</code> to the first byte of the file.  I want to write <code>0x02</code> to every byte.
I also tried:
<code>m[:] = bytes(1)
</code>
But this also only writes to the first byte.
When I try <code>m[0] = b'\x02'</code>, it writes to the first byte as expected.  When I try to use a range:
<code>m[0:1] = b'\x02'
</code>
I get a <code>ValueError: slice assignment is not supported</code>
When I try to use a slice:
<code>m[:] = b'\x02'[:1]
</code>
I get a <code>BufferError: cannot modify size of memory mapping</code>
I am using Python 3.6.4


A:

<code>m = mmap.
