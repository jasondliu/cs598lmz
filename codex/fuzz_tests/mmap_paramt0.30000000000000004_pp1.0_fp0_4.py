import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.close()
</code>
This works, but I want to know if there is a better way to do this.


A:

You can use <code>mmap.ACCESS_COPY</code> to create a copy-on-write memory map.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
    m.write(bytes(1))
    m.close()
</code>

