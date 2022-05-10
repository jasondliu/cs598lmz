import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ|mmap.PROT_WRITE)
    print(m.seek(0))
    print(m.write(bytes(3)))
    print(m.read(1))
