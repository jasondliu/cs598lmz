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
