import mmap
# Test mmap.mmap
with open('file.mmap', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 6)  # copy 6 bytes from offset 0
    print(m)
    # close the mmap object
    m.close()

# Save
with open('file.mmap', 'w+b') as f:
    # copy 6 bytes from offset 0
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(b'Hello')
    # close the mmap object
    m.close()


# Read file
with open('file.mmap', 'r+b') as f:
    # copy 6 bytes from offset 0
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.read(6))
    # close the mmap object
    m.close()


# Test mmap.mmap
with open('file.mmap', 'r+b') as f:
    m
