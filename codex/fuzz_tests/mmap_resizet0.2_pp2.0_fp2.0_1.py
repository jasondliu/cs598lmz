import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line raises <code>ValueError: mmap closed or invalid</code>.
I'm using Python 3.6.1 on Windows 10.
Is this a bug?


A:

This is a bug in Python 3.6.1. It was fixed in Python 3.6.2.

