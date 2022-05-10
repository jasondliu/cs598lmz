import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code will print <code>b'\x01'</code> on Python 3.4 and 3.5, but <code>b''</code> on Python 3.6 and 3.7. The documentation says that the mapping is invalidated on file truncation, but it doesn't say that it's invalidated on file truncation to zero length.
Is this a bug in Python or am I missing something?


A:

This is a bug in Python 3.6 and 3.7. Python 3.4 and 3.5 are not affected.
The bug was fixed in Python 3.8.

