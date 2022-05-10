import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
If you don't have a file, you can use <code>mmap.mmap(-1, size)</code> to create an anonymous memory-mapped file.

