import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
With Python 3.3, <code>a</code> is equal to <code>b'\x01'</code>.
With Python 2.7.9, <code>a</code> is equal to <code>b''</code> (i.e. the truncation is not reflected in the mmap).
Is this a bug in Python 2.7, or is it how the API is supposed to work?


A:

As of Python 2.7.10, this is now fixed.

