import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    while True:
        s = m.readline()
        if not s:
            break
        print(s)
    m.resize(2**20)   # this is beautiful!
    m.close()
