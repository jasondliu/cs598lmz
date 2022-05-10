import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    # This can be fixed by adding:
    # m.seek(0)
</code>
The broken case is the same as the working case, except that the file is opened in <code>r+b</code>, not <code>rb</code>. The difference is that <code>r+b</code> keeps the file open for writing.
The bug is that <code>m[:]</code> does a <code>read</code> on the file descriptor, which fails when the file is open for writing.

