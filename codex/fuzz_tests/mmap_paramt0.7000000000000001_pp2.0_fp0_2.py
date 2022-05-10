import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m[0] = bytes(2)
    m.close()
</code>
This gives me this error:
<code>m[0] = bytes(2)
TypeError: 'mmap.mmap' object does not support item assignment
</code>
What am I doing wrong?


A:

The problem is that the mmap object doesn't support item assignment. You need to use the write method like this:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.write(bytes(2))
    m.close()
</code>

