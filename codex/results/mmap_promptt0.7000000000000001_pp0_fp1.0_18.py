import mmap
# Test mmap.mmap(0,1)
with mmap.mmap(0, 1) as m:
    print m.read(1)

# Test mmap.mmap(-1,1)
with mmap.mmap(-1, 1) as m:
    print m.read(1)

# Test mmap.mmap(0,0)
with mmap.mmap(0, 0) as m:
    print m.read(1)

# Test mmap.mmap(-1,0)
with mmap.mmap(-1, 0) as m:
    print m.read(1)

# Test mmap.mmap(0,1,fileno=100)
with mmap.mmap(0, 1, fileno=100) as m:
    print m.read(1)

# Test mmap.mmap(-1,1,fileno=100)
with mmap.mmap(-1, 1, fileno=100) as m:
    print m.read(1)

# Test mmap.mmap(0,0,fileno
