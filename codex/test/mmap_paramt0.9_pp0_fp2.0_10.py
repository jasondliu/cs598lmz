import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)

    # Increment by one the first byte
    m[0] = ord(m[0:1]) + 1

