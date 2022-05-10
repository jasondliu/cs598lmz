import mmap
# Test mmap.mmap(0, size, flags, prot, access)
m=mmap.mmap(0, 1024, "MAP_SHARED", mmap.ACCESS_READ | mmap.ACCESS_WRITE)
# Test mmap.mmap(0, size, prot=mmap.PROT_READ | mmap.PROT_WRITE, flags=mmap.MAP_SHARED)
m=mmap.mmap(0, 1024)
