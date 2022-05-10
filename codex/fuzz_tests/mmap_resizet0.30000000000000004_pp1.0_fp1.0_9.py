import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect <code>a</code> to be empty, but it contains <code>b'\x01'</code>.
I've also tried <code>m.resize(0)</code> and <code>m.resize(1)</code> before reading, but the result is the same.
I'm using Python 3.6.5 on Windows 10.

