import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    # --- add 'r' or 'w' here as well in the line below
    mprot = mmap.ACCESS_READ | mmap.ACCESS_WRITE
    m.resize(100, mprot)
