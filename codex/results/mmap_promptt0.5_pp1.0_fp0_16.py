import mmap
# Test mmap.mmap()
#
# Create a file for testing
file = open('mmap_file', 'w+')
file.write('\0' * 1024)
file.close()

# Open the file
file = open('mmap_file', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(file.fileno(), 0)
print 'mmap()', m

# Read the content via standard file methods
print 'First 10 bytes via read :', m.read(10)
print 'First 10 bytes via slice:', m[:10]
print '2nd   10 bytes via read :', m.read(10)
print '3rd   10 bytes via read :', m.read(10)

# Update content using slice notation;
# note that new content must have same size
m[6:] = 'world'
m.seek(0)  # rewind
print 'First 10 bytes via read :', m.read(10)

# Close the map
m.close()

# Verify that changes were made
file =
