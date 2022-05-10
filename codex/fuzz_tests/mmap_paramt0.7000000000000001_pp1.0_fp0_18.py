import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[3] = 1
    m.close()
    print(f.tell())
    f.seek(3)
    print(f.read(1))
