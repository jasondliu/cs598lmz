import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect the last line, <code>a = m[:]</code> to raise a <code>ValueError</code> as the file on disk is truncated, but instead it succeeds. Is this a bug?

