import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    for i in range(len(m)):
        m[i] = b'X'

with open('test', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    tr_x = m.translate(chr(10).encode())
    print(m.encode())
    m.close()
with open('ff.txt', 'w') as f:
    f.write('\n')

with open('ff.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    for i in range(4):
        print(m[i])
