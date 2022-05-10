import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print(m[:])
    m[:] = bytes(2)
    m.flush()
    print(m[:])
    
os.remove('test')
