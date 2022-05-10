import mmap
# Test mmap.mmap()

# Create a file of 100 bytes
with open("testfile", "wb") as f:
    f.write(b"\x00" * 100)

# Open the file for reading
with open("testfile", "r+b") as f:
    # Create a memory-map of the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0)
    # Read the content via standard file methods
    print(m.read(10))
    # Update the file from the memory-map
    m.seek(0)
    m.write(b"ABCDE")
    # Close the memory-map
    m.close()

# Open the file for reading
with open("testfile", "rb") as f:
    # Read the whole file at once
    print(f.read())

# Open the file for reading
with open("testfile", "r+b") as f:
    # Memory-map the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0)
    # Print
