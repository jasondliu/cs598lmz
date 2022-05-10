import mmap
# Test mmap.mmap()

# Open a file for writing and create it if it doesn't exist
# f = open("hello.dat", "w+")

# Open the file for reading and writing
f = open("hello.dat", "r+")

# Create a memory map on the file.
# Since the file has zero size, the entire file is
# mapped to a zero-length region.  Any attempts to
# access beyond the end of the file will raise an
# exception.
m = mmap.mmap(f.fileno(), 0)

# Write a byte at offset 0.
print("Write a byte at offset 0.")
m.write( b"a" )

# Close the map, and the file is closed
m.close()
