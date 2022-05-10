import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[0] = 0  # changes the value at index 0
    m.close()

with open('test', 'rb') as f:
    print(f.read())
