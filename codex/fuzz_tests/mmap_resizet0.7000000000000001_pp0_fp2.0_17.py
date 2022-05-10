import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be equal to <code>bytes(1)</code>, but it is <code>b''</code>. The same happens if I use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)</code>.
Am I doing something wrong?

