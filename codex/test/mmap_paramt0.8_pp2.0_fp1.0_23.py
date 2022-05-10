import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 2)
    m[0] = b'\x00'
    m[1] = b'\xff'
    m.close()

with open('test', 'rb') as f:
    print(f.read())
