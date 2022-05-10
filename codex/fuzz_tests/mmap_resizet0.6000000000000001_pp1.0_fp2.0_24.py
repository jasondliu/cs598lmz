import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This is a problem for me, because I don't have access to the file object, and I can't just call <code>f.close()</code> on it.  It is a socket file, so I'm not sure if that has anything to do with it.


A:

<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
</code>

