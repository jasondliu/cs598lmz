import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b'\x01'</code> on Python 3.6.5, but <code>b''</code> on Python 3.7.0.
Is this a bug in Python 3.7.0?


A:

This is a bug in Python 3.7.0. It has been fixed in Python 3.7.1.

