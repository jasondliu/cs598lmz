import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b''</code> on Python 3.5.2, but <code>b'\x01'</code> on Python 3.6.3.
Is this a bug in Python 3.5.2, or is it expected behavior?

