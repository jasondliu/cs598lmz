import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This gives me a <code>ValueError: mmap offset is greater than file size</code>
I am using Python 3.6.5 on Linux.
How can I truncate the file without getting this error?


A:

The problem is that <code>mmap</code> is not aware of the file being truncated.
You can use <code>m.resize(0)</code> to shrink the mmap to 0 bytes.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
    print(a)
</code>

