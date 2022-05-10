import mmap
# Test mmap.mmap(0,1)
with mmap.mmap(0,1) as m:
    print(m[0:10])

# Test mmap.mmap(-1,1)
with mmap.mmap(-1,1) as m:
    print(m[0:10])

# Test mmap.mmap(-1,1,mmap.MAP_SHARED,mmap.PROT_READ)
with mmap.mmap(-1,1,mmap.MAP_SHARED,mmap.PROT_READ) as m:
    print(m[0:10])

# Test mmap.mmap(-1,1,mmap.MAP_SHARED,mmap.PROT_WRITE)
with mmap.mmap(-1,1,mmap.MAP_SHARED,mmap.PROT_WRITE) as m:
    print(m[0:10])

# Test mmap.mmap(-1,1,mmap.MAP_SHARED,mmap.PROT_EXEC)
with mmap.mm
