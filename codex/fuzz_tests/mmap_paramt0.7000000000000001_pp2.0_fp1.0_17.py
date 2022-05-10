import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
But it fails with error <code>TypeError: an integer is required (got type bytes)</code>
How do I do it?


A:

<code>bytes</code> is an immutable sequence of bytes. It can be created from an iterable of integers, each in the range 0 to 255.
To create a mutable object of bytes, you should use <code>bytearray</code> instead:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytearray([2])
</code>

