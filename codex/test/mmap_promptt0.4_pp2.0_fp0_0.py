import mmap
# Test mmap.mmap()

# Open file for reading
with open('lorem.txt', 'r') as f:
    # Create memory-map to file
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Read from memory-map and print
    print(m.readline())
    # Close memory-map
    m.close()

# Open file for writing
with open('lorem.txt', 'r+') as f:
    # Create memory-map to file
    m = mmap.mmap(f.fileno(), 0)
    # Write to memory-map
    m.write(b'0123456789abcdef')
    # Read from memory-map and print
    m.seek(0)
    print(m.read(16))
    # Close memory-map
    m.close()

# Open file for writing
with open('lorem.txt', 'r+') as f:
    # Create memory-map to file
    m = mmap.mmap(f.fileno(), 0)

