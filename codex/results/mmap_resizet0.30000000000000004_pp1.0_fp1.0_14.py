import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be <code>bytes(1)</code>, but it is <code>bytes(0)</code>.
I am using Python 3.6.3 on Windows 10.

