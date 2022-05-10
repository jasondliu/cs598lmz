import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(5))
    m.close()


with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(len(m))
    print(m[1])
    m.close()
