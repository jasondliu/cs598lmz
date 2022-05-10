import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m.write_byte(bytes(1))
</code>
This code fails with <code>TypeError: a bytes-like object is required, not 'int'</code>
If I try to use an integer, I get a similar error.
<code>m.write_byte(1)
</code>
gives
<code>TypeError: an integer is required
</code>
Is it possible to do byte-by-byte manipulation with <code>mmap</code> in Python 3?


A:

The <code>write_byte()</code> method takes an integer, not a bytes-like object. The integer value should be in range 0-255 and represents the byte to be written.
<code>m = mmap.mmap(f.fileno(), 1)
m.write_byte(1)
</code>

