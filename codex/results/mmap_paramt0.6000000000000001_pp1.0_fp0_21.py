import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)

    m[0] = b'\x1'
    print(m.read(1))

    # m[0] = b'\x1'  # It will raise ValueError: byte must be in range(0, 256).
    # print(m.read(1))

    m[0] = 1
    print(m.read(1))

    m[0] = ord(b'\x1')
    print(m.read(1))
</code>

