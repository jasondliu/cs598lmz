import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
I get <code>TypeError: memoryview: a bytes-like object is required, not 'mmap.mmap'</code>.
If I use <code>m.read()</code> instead, it works as expected.

