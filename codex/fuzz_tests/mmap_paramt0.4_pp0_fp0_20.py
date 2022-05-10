import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 48
</code>
But I'm getting <code>TypeError: 'mmap.mmap' object does not support item assignment</code>. What's wrong?


A:

The <code>mmap</code> object is read-only by default.  You need to specify <code>access=mmap.ACCESS_WRITE</code> when you create the object.

