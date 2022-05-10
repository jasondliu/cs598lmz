import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline().decode('utf8'))
    m.write(b'2')
    m.seek(0)
    print(m.readline().decode('utf8'))
    m.close()
