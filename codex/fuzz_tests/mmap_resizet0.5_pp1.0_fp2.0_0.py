import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I'm expecting that <code>a</code> will be <code>bytes(1)</code>, but it's <code>b''</code>.
If I change <code>f.truncate()</code> to <code>f.truncate(2)</code> or <code>f.truncate(1)</code> it works.
How can I truncate file to 0 bytes in this case?

