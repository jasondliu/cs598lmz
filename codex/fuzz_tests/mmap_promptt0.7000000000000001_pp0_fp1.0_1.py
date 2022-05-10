import mmap
# Test mmap.mmap()
# Test mmap.mmap(fileno, length)
# Test mmap.mmap(fileno, length, flags=MAP_PRIVATE, prot=PROT_READ, access=ACCESS_COPY)

# Create a new empty file to back the mmap
with open(filename, 'w') as f:
    pass

# Create the mmap with the following params:
#   fileno - The file descriptor of the file that we want to map
#   length - The number of bytes to map.
#   flags - mmap flags. MAP_PRIVATE creates a copy-on-write mapping, so changes
#           to the contents of the mmap object will be private to this process.
#   prot - mmap protection. PROT_READ ensures that pages may be read.
#   access - The memory access pattern. This is ignored on Windows.
with open(filename, 'r+') as f:
    with mmap.mmap(f.fileno(), 0,
                   access=mmap.ACCESS_WRITE) as m:
        # Print the length of the mapped region
