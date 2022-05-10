import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

# Keep reference to m and see what happens.
</code>


A:

You can create a new object that reference the same memory, like so:
<code>m2 = mmap.mmap(m.fileno(), 0, access=m.access, offset=m.offset)
</code>
There is no such method on the object, but it is easy to implement.

