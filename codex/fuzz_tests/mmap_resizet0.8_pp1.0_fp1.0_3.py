import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises <code>ValueError: cannot mmap beyond last file offset</code>.
So far I've found two options to work around this.
First one is to use <code>msync(0)</code> before truncating.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.msync(0)
    f.truncate()
    a = m[:]
</code>
The other is to disconnect from the file by calling <code>madvise(MADV_DONTNEED)</code>.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.madvise(mmap.MADV_DONTNEED)
    f.truncate()
    a = m[:]
</code>
Are there any other options to work around this problem?

