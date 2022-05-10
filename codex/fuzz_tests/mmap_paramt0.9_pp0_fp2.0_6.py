import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = 2
    m.close()

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(str(m[0]))  # 2
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(1))  # 1
    m.write(bytes(1))  # 1
    m.write(bytes(1))  # 1
    m.close()

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(int(m[0]))  # 1
    print(int(m[1]))  # 1
    print(int(m[2]))  #
