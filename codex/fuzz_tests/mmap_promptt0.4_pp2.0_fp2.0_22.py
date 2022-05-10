import mmap
# Test mmap.mmap(fileno, length, access, offset)
# access is one of ACCESS_READ, ACCESS_WRITE, ACCESS_COPY, ACCESS_DEFAULT
# ACCESS_READ: read-only, no changes allowed
# ACCESS_WRITE: read-write, changes allowed
# ACCESS_COPY: copy-on-write, changes allowed but not written to file
# ACCESS_DEFAULT: same as ACCESS_READ

# offset is the offset from the start of the file

# mmap.mmap(fileno, length, access, offset)

# fileno is the file descriptor of the file to be mapped
# length is the number of bytes to be mapped
# access is one of ACCESS_READ, ACCESS_WRITE, ACCESS_COPY, ACCESS_DEFAULT
# offset is the offset from the start of the file

# mmap.mmap(fileno, length, access, offset)

# fileno is the file descriptor of the file to be mapped
# length is the number of bytes to be mapped
# access is one of ACCESS_READ
