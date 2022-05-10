import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print('mmap before:', m[:1])
    m[:1] = b'\00'
    m.flush()
    m.close()

