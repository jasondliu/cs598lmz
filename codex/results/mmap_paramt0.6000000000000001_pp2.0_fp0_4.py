import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = bytes(2)
</code>
It raises:
<code>ValueError: memoryview: invalid slice key
</code>
I also tried using <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE, offset=0)</code> but it doesn't work either.


A:

I found a workaround by using <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE, offset=0)</code> and <code>m[0:1] = bytes(2)</code> instead of <code>m[0] = bytes(2)</code>.

