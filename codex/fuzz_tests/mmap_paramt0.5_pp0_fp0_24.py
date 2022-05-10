import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x00')
    m.seek(0)
    m.write(b'\x01')
    m.seek(0)
    print(m.read(1))
    m.close()
</code>

