import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print('before:', m.read(1))
    m.write_byte(b'c')
    print('after:', m.read(1))
    m.close()
