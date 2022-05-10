import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ | mmap.PROT_WRITE)
    while True:
        b = m.read_byte()
        if b == 0x1e:
            print(m.tell())
            m.seek(0, 0)
            m.write_byte(0x1f)
            break
    m.close()
