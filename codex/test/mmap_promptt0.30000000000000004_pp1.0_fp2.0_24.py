import mmap
# Test mmap.mmap
# mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0)
# Open the file for reading.
f = open('lorem.txt', 'r')
# Create a memory-map to the file, size 0 means whole file.
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# Print the content via the memory-mapped file.
print(m.readline())
# Close the memory-mapped file.
m.close()
# Close the underlying file.
f.close()

# Test mmap.mmap
# mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0)
# Open the file for reading.
f = open('lorem.txt', 'r')
# Create a memory-map to the file, size 0 means whole file.
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
