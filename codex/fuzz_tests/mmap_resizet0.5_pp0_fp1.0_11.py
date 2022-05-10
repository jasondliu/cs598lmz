import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This will print <code>b'\x01'</code> on Python 3.5 and <code>b''</code> on Python 3.6.

