import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print(m)
    m[0] = b'2'
    m.close()
</code>
Output:
<code>&lt;mmap.mmap object at 0x10c327750&gt;
</code>
The problem is, the <code>bytes</code> object cannot be changed by <code>mmap</code>.

