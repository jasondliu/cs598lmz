import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(1)
    m.seek(0)
    assert m.read_byte() == 1
</code>

