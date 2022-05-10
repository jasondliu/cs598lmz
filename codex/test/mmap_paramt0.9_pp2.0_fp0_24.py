import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)  # seek to beginning of file
    m[0] = bytes(1)  # change the first byte in file
