import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In the line with <code>a = m[:]</code> I get a SIGBUS signal. Why?


A:

The mmap() documentation explicitly states that it may not work at all if you truncate the file. If a file is mapped with MAP_SHARED, depending on implementation details, it may affect the size of the underlying object and thus invalidate the mapping.
When you truncate the file, the mapping is invalid.

