import mmap
# Test mmap.mmap()

# Create a file and open it for writing
f = open('test.txt', 'w+')

# Write the string '0123456789' to the file
f.write('0123456789')

# Close the file
f.close()

# Open the file for reading
f = open('test.txt', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read the content via standard file methods
print 'First 10 bytes via read :', m.read(10)

# Read the content via slice notation
print 'First 10 bytes via slice:', m[:10]

# Update the slice
# Note that new content must have same size
m[:11] = 'Hello World'

# See what the file contains
m.seek(0)
print m.readline()

# Close the mmap object
m.close()

# Close the file
f.close()

# Open the file for reading
f = open('test.txt', 'r+')

#
