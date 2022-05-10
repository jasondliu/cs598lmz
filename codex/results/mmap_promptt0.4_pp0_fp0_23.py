import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# Open the file for reading
f = open('lorem.txt', 'r')
# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# Print the file
print(m.readline())
# Close the map
m.close()
# Close the file
f.close()

# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# Open the file for reading
f = open('lorem.txt', 'r')
# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# Print the file
print(m.readline())
# Close the map
m.close()
# Close the file
f.close()
