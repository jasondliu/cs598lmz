import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    #m.close()
    #f.close()

with open('test', 'rb') as f:
    a = f.read()
    print(a)
    f.close()
