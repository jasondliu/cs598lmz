import mmap
# Test mmap.mmap.read

# Create a file
with open("test.txt", "wb") as f:
    f.write(b"Hello, world")

# Open the file for reading
with open("test.txt", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Read the entire file
    print(m.read())

# Close the map
m.close()
