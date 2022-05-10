import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'1')
    m.write(b'2')
    m.write(b'3')
    m.write(b'4')
    m.write(b'5')
    m.write(b'6')
    print(m[:])
    m.close()
