import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 12
</code>
This gives me "ValueError: byte must be in range(0, 256)".
What's the problem with that?


A:

The problem here is that in Python 2 <code>bytes</code> is a string type, not an integer. <code>bytes</code> is an immutable sequence of integers in the range 0..255 representing bytes. To write a single byte to a file, you can use the <code>struct.pack()</code> function.
To write a single byte at a position in the file, use:
<code>import mmap
import struct

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = struct.pack('&gt;B', 12)
</code>
The <code>'&gt;'</code> prefix tells the <code>struct</code> module to use big-endian byte ordering.
If you
