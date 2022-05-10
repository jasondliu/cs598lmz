import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be <code>b'\x00'</code>, but it's <code>b'\x01'</code>.
I'm using Python 3.6.4 on Windows 10.
Is this a bug in Python or Windows?

