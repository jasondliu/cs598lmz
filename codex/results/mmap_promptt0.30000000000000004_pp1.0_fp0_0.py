import mmap
# Test mmap.mmap()

# Open file
with open("test.txt", "w+") as f:
    # Create mmap object
    m = mmap.mmap(f.fileno(), 0)
    # Write to mmap
    m.write("Hello world!")
    # Read from mmap
    print(m.readline())
    # Close mmap
    m.close()

# Test mmap.mmap()

# Open file
with open("test.txt", "w+") as f:
    # Create mmap object
    m = mmap.mmap(f.fileno(), 0)
    # Write to mmap
    m.write("Hello world!")
    # Read from mmap
    print(m.readline())
    # Close mmap
    m.close()

# Test mmap.mmap()

# Open file
with open("test.txt", "w+") as f:
    # Create mmap object
    m = mmap.mmap(f.fileno(), 0)
    # Write to mmap
    m.write
