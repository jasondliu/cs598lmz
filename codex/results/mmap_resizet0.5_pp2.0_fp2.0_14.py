import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be empty, but it is <code>b'\x01'</code>.
Why is this?


A:

When you truncate the file, the memory mapping is still valid, and it is still pointing to the same memory location. The memory location is still valid, but the data there is now garbage.
There is no way to invalidate the mapping because the file has been truncated.

