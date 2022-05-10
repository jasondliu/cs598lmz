import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'a')
    print(m)
</code>
<code>m</code> is a buffer object and it is different from a regular Python list. It is also different from a <code>str</code> object. It does not support indexing. It does not support negative indices. It does not support slice assignment. If you want to change something inside a buffer object, you have to use the <code>write</code> method.

