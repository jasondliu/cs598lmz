import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    print(m[0])
    print(m[0:])
    print(m[1:])
    print(m[:])

    m.write(b'2')
    print('wrote 2')
    print(m[0])

    m.seek(0)
    print('seek 0')
    print(m[0])
