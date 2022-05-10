import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
But in this case i have a <code>TypeError: write() argument must be str, not int</code>
How to write a single byte to file using mmap?


A:

<code>bytes</code> is an immutable type. <code>m[0] = b'\x00'</code> is trying to mutate the first byte of the <code>bytes</code> object, which is not allowed.
You can write to a <code>bytearray</code> instead:
<code>with open('test', 'wb') as f:
    f.write(bytearray(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>

