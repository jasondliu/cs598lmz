import mmap
# Test mmap.mmap()
filename = os.path.join(tempfile.gettempdir(), 'newfile.txt')
with open(filename, 'w') as f:
    f.write('Hello World!')
with open(filename, 'r') as f:
    with mmap.mmap(f.fileno(), 0,
                   access=mmap.ACCESS_READ) as m:
        print('First 10 bytes via read :', m.read(10))
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY) as m:
        print('First 10 bytes via slice:', m[:10])
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) as m:
        print('First  5 bytes via write:', m[:5])
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) as m:
        m[6:] = b'WORLD!'
