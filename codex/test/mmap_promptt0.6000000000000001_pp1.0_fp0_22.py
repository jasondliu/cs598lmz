import mmap
# Test mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_READ|PROT_WRITE, access=ACCESS_DEFAULT, offset=0)
# -> mmap.ACCESS_COPY
# -> mmap.ACCESS_READ
# -> mmap.ACCESS_WRITE
# -> mmap.ACCESS_DEFAULT

# -> mmap.PROT_NONE
# -> mmap.PROT_READ
# -> mmap.PROT_WRITE
# -> mmap.PROT_EXEC

# -> mmap.MAP_SHARED
# -> mmap.MAP_PRIVATE
# -> mmap.MAP_ANONYMOUS
# -> mmap.MAP_ANON
# -> mmap.MAP_DENYWRITE
# -> mmap.MAP_EXECUTABLE
# -> mmap.MAP_GROWSDOWN
# -> mmap.MAP_LOCKED
# -> mmap.MAP_NONBLOCK
# -> mmap.MAP_NORESERVE
# -> mmap.MAP_POPULATE

