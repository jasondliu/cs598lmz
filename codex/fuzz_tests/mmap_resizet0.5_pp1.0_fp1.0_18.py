import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected that <code>a</code> would be <code>bytes(1)</code>, but it is actually <code>bytes(0)</code>. I think this is because <code>mmap</code> is not updated after <code>truncate</code>.
Is there any way to update <code>mmap</code>?

