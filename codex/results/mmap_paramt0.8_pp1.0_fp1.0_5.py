import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m[0])
    m[0] = 2
    m.flush()
    print(m[0])
</code>
<code>2</code> is not written to file.


A:

<code>mmap.mmap()</code>creates a file-backed memory map. Using <code>mmap.ACCESS_WRITE</code> access type allows you to write to it, but you will not see the changes on disk until you call <code>mmap.mmap.flush()</code> explicitly.

