import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:len(bytes(1))] = bytes(1)
    m.flush()
    m[0:len(bytes(2))] = bytes(2)

with open('test', 'rb') as f:
    print(f.read())
