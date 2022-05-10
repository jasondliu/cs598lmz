import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 48

del m

with open('test', 'rb') as f:
    print(ord(f.read()[0]))
