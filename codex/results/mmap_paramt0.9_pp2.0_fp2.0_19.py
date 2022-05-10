import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    while True:
        buffer = m.read(1)
        if not buffer:
            break
        print int(buffer)
        m.seek(0)
        m.write(bytes(int(buffer) + 1))
    m.flush()

with open('test2.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    while True:
        buffer = m.read(1)
        if not buffer:
            break
        print buffer
        m.seek(0)
        m.write('O')
    m.flush()
