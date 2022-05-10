import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'1'  # TypeError: an integer is required
    m[0] = bytes([49])  # TypeError: an integer is required
</code>
It's possible to manually convert the right side of the <code>=</code> operator with the following snippet,
<code>    byte_type = type(bytes([0]))
    m[0] = byte_type(b'1')
</code>
but it is also not very convenient.
How can I avoid manual conversion?

