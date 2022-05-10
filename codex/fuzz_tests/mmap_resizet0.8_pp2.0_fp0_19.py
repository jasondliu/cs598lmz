import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives me:
<code>ValueError: mmap can't extend memory maps backed by file objects
</code>
I've tried <code>m.close()</code> before the <code>truncate()</code> as well, which gives me:
<code>ValueError: mmap closed or invalid
</code>
How do I truncate a file while I have an open <code>mmap</code> to it?


A:

This seems to work for me:
<code>with open('test', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.resize(0)
</code>

