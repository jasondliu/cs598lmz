import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), length=1, access=mmap.ACCESS_WRITE)
    m.write_byte(b'a')
    m.flush()
</code>

