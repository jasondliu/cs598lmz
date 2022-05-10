import mmap
# Test mmap.mmap()

# Create a memory-mapped file, size 0
m = mmap.mmap(-1, 0)
# Write a byte at offset 0
m.write(b'x')
# Read a byte at offset 0
print(m[0])
# Close the memory-mapped file
m.close()

# Create a memory-mapped file, size 0
m = mmap.mmap(-1, 0)
# Write bytes at offsets 0, 1, 2, 3
m[0:4] = b'abcd'
# Read a byte at offset 0
print(m[0])
# Read bytes at offsets 0, 1, 2, 3
print(m[0:4])
# Close the memory-mapped file
m.close()

# Create a memory-mapped file, size 0
m = mmap.mmap(-1, 0)
# Write bytes at offsets 0, 1, 2, 3
m[0:4] = b'abcd'
# Read bytes at offsets 0, 1, 2, 3
print(m[0:4])
# Read bytes at
