import mmap
# Test mmap.mmap

# Create a file with a fixed size
f = open("test.txt", "w+")
f.write("Hello World")
f.seek(1024 * 1024 * 1024)
f.write("EOF")
f.close()

# Open the file
f = open("test.txt", "r+")

# Memory map the file
m = mmap.mmap(f.fileno(), 0)

# Read the first 10 bytes
print(m[:10])

# Close the file
f.close()

# Un-memory-map the file
m.close()

# Delete the file
