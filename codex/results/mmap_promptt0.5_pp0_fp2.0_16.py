import mmap
# Test mmap.mmap()
#
# Create a file that will be used as a memory-mapped object.
fp = open('lorem.txt', 'r+')
fp.write('0123456789abcdef')
fp.close()
# Open the file for reading and writing.
f = open('lorem.txt', 'r+')
# Create a memory-map to the file.
m = mmap.mmap(f.fileno(), 15)
# Print the original contents.
print m.readline()
# Update a slice of the memory-mapped file.
m[5:10] = 'xxxxx'
# Read from the memory-mapped file again.
m.seek(0)
print m.readline()
# Close the memory-mapped file.
m.close()
# Close the underlying file.
f.close()
