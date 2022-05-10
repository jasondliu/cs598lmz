import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 1024)
# Memory map files
m = mmap.mmap(f.fileno(), 1024)
m = mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_READ)
# Map anonymous memory
m = mmap.mmap(-1, 1024)
# Map a file, creating it if necessary
m = mmap.mmap(fileno, length, flags=mmap.MAP_SHARED, prot=mmap.PROT_WRITE, access=mmap.ACCESS_WRITE)
# Map a file, creating it if necessary
m = mmap.mmap(fileno, length, flags=mmap.MAP_SHARED, prot=mmap.PROT_WRITE, access=mmap.ACCESS_WRITE)
# Map a file, creating it if necessary
m = mmap.mmap(-1, 1024)
