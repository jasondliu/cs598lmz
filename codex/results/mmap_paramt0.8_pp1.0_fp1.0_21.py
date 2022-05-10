import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x02')
    m.seek(0)
    print([hex(c) for c in m])
    m.close()
