import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    m.write(bytes(1))
    m.seek(0)
    print(m.read())
</code>
or more simply:
<code>with open('test', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    m.write(bytes(1))
    m.seek(0)
    print(m.read())
</code>

