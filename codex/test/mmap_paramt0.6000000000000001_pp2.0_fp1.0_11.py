import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    #  m[:] = b'\x00'
    m[0:1] = b'\x00'
    m[1:2] = b'\x00'
    m.close()
