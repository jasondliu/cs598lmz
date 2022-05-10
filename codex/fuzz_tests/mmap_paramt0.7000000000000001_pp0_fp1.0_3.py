import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.size())  # 1
    m[0] = 50

with open('test', 'rb') as f:
    data = f.read()
    print(data)  # b'2'
</code>

