import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    print(ord(m[0]))
    m[0] = bytes(2)
    print(m[:])
    print(ord(m[0]))
    print(bytes(ord(m[0])) == m[:])
    print(hash(m[:]) == hash(bytes(ord(m[0]))))
print(bytes(ord(m[0])) == m[:])
