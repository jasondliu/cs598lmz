import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm expecting a to be an empty byte string, but instead it is b'\x01'. I'm running Python 3.6.5 on Ubuntu 18.04.

