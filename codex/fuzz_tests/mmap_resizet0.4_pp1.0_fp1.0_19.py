import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected that the <code>a</code> variable will be <code>b''</code>, but it is <code>b'\x01'</code>.
Why?

