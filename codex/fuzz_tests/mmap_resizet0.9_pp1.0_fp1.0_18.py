import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Given the above code, <code>a</code> will not be an empty list.
I know the file doesn't need to get mapped twice, but is this expected behavior? I would think that <code>m</code> would be updated when <code>f</code> gets truncated.

