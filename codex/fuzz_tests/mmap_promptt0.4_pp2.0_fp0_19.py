import mmap
# Test mmap.mmap()

# mmap.mmap(fileno, length, access=mmap.ACCESS_DEFAULT, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, offset=0)

# fileno: File descriptor of the file to map.
# length: Number of bytes to map.
# access: mmap.ACCESS_READ, mmap.ACCESS_WRITE, or mmap.ACCESS_COPY.
# flags: mmap.MAP_SHARED or mmap.MAP_PRIVATE
# prot: mmap.PROT_EXEC, mmap.PROT_READ, mmap.PROT_WRITE, or mmap.PROT_NONE
# offset: Offset into the file to start the mapping.

# mmap.ACCESS_READ: Read-only access.
# mmap.ACCESS_WRITE: Write-only access.
# mmap.ACCESS_COPY: Copy-on-write access.

# mmap.MAP_SHARED: Changes are shared.
# mmap.MAP_
