import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    print(m[1]) # returns 0 (the byte value)
    print(m[2]) # returns 0 (the byte value)
