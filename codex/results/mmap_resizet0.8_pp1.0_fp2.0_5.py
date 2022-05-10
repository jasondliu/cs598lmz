import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
raises
<code>mmap.error: [Errno 22] Invalid argument
</code>
Truncating before mmap works as expected, but truncating after mmap does not work. Why? Is it possible to truncate after mmap?
(I'm testing on Python 3.6)


A:

I did not expect this to work:
<code>m = mmap.mmap(f.fileno(), 0)
</code>
Was surprised to see this work as expected:
<code>m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
</code>
See: https://docs.python.org/3/library/mmap.html

