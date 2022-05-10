import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE)
    m[0] = b'2'
    print(bytes(m[0]))
    m.close()
</code>

