import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\0')
    m.seek(0)
    m.write(b'\1')
    m.flush()

with open('test', 'rb') as f:
    print(f.read())

