import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Output is <code>b'\x01'</code>
But I expect empty string.
What am I doing wrong?


A:

<code>mmap.mmap</code> does not automatically resize when you change the file size. You need to call the <code>resize</code> method after truncating the file (or before truncating it, if you want to avoid the data loss).
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1)
    f.truncate()
    a = m[:]
    print(a)
</code>

