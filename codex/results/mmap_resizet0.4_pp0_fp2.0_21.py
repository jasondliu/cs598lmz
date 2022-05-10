import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This causes a segfault. I would expect that <code>m[:]</code> would return an empty string. I am using Python 2.7.5 on Ubuntu 14.04.

