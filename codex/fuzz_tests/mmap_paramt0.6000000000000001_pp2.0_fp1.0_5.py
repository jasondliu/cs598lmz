import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('2')
    m.close()
</code>


A:

You can use <code>mmap.ACCESS_WRITE</code> to open the file in read/write mode.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = ord('2')
    m.close()
</code>

