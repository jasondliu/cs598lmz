import mmap
# Test mmap.mmap()
# https://docs.python.org/2/library/mmap.html

# Open a file
f = open('/tmp/test.txt', 'r+')
# Create a memory-map to an int-sized portion of the file
map = mmap.mmap(f.fileno(), 0)
# Write a byte at offset 0
map.write('test')
# Close the map and file
map.close()
f.close()

# Open the file for reading
f = open('/tmp/test.txt', 'r')
# Print the (decoded) bytes at offset 0
print(f.readline())
# Close the file
f.close()

# Open the file for reading
f = open('/tmp/test.txt', 'r')
# Create a memory-map to an int-sized portion of the file
map = mmap.mmap(f.fileno(), 0)
# Read the contents of the file, one byte at a time
print(map.readline())
# Close the map and file
map.close()
f.close()

#
