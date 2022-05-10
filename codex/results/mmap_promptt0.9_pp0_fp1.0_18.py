import mmap
# Test mmap.mmap

with open('/proc/loadavg', 'r') as f:
    M = mmap.mmap(f.fileno(), 0, 1, mmap.MAP_SHARED, mmap.PROT_READ)

    s = M.read(1)
    print(type(s))
    print(repr(s))
    s = M.read(2)
    print(type(s))
    print(repr(s))
    s = M.read(3)
    print(type(s))
    print(repr(s))
    
    M.close()
# Test mmap.mmap

with open('/proc/loadavg', 'r') as f:
    M = mmap.mmap(f.fileno(), 0, 1, mmap.MAP_SHARED, mmap.PROT_READ)

    s = M.read(5)
    print(repr(s))

    M.seek(0)
    
    s = M.read(3)
    s = M.read(2)

