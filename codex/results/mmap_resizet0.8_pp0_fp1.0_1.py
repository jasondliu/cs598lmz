import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] #This line throws ValueError: mmap closed or invalid
</code>

Python 2.7.5
Ubuntu 14.04

Why does the line <code>a = m[:]</code> throw a <code>ValueError</code>?

