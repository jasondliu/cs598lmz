import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = ord('#')
</code>
You can also do the same with multiple bytes
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(10))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = bytes([1, 2, 3, 4, 5])
</code>

