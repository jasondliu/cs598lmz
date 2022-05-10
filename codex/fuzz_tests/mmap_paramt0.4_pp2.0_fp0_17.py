import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
But I need to do this in a more memory efficient way.
I tried using <code>mmap.mmap</code> directly:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with mmap.mmap(-1, 1, 'test', mmap.ACCESS_WRITE) as m:
    m[0] = 0
</code>
But this fails with <code>OSError: [Errno 22] Invalid argument</code>.
Is there a way to use <code>mmap.mmap</code> to do this without reading the whole file into memory?

