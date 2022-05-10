import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
This code will print <code>b'\x01'</code> on Python 3.6.4, but <code>b''</code> on Python 3.7.0.
I've tried to look for a change in Python 3.7 that would explain this, but I can't find anything.
Is this a bug in Python 3.7?


A:

In Python 3.6, <code>mmap</code> objects were not garbage collected until the process exits. This was a bug, and it was fixed in Python 3.7.

