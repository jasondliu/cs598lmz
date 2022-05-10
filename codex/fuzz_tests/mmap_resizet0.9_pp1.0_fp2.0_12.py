import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # or similar
</code>
The <code>mmap</code> access would fail with a <code>ValueError</code> though - so if you wanted to continue using <code>mmap</code>, you would need to be careful which code you execute in case of a crash.

