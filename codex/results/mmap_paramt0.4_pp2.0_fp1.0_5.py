import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
</code>
If you want to use <code>mmap</code> with <code>open</code>'s <code>buffering</code> parameter, you will need to use <code>mmap.ACCESS_COPY</code> and <code>mmap.ACCESS_WRITE</code> (or <code>mmap.ACCESS_DEFAULT</code>).
<code>with open('test', 'r+b', buffering=0) as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
</code>

