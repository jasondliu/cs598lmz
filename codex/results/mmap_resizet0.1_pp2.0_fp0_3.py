import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b'\x01'</code> on Python 3.5.2, but <code>b''</code> on Python 3.6.1.
I think this is a bug, but I'm not sure.
Is this a bug?


A:

This is a bug in Python 3.6.1.
It was fixed in Python 3.6.2.

