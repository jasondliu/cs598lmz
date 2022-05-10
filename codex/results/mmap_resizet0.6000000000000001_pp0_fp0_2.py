import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this example, it's not necessary to call <code>m.flush()</code> after <code>f.truncate()</code> because the <code>mmap</code> object is not modified.

