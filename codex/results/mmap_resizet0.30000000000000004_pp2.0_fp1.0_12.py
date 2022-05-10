import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be an empty array, but it is not.
I am using Python 3.6.1.


A:

This is a bug in Python 3.6.1. It is fixed in Python 3.6.2.

