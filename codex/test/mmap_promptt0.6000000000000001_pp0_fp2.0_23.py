import mmap
# Test mmap.mmap and mmap.ACCESS_READ

# Create a file and memory-map it
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")
f = open("hello.txt", "rb")
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print the content via standard file methods
print(f.readline())

# Print the content via the mmap module
print(m.readline())

# Close the map and the file
m.close()
f.close()
