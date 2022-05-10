import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect <code>a</code> to be <code>b'\x01'</code>, but it's <code>b''</code>.
I'm on Python 3.6.2 on Windows 10.

