import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code will print <code>b''</code> on Python 3.6.4, but <code>b'\x01'</code> on Python 3.5.2.
I'm not sure if this is a bug or a feature.

