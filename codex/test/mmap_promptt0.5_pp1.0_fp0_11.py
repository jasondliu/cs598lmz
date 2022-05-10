import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read some data
print('First 10 bytes via read :', m.read(10))

# Reset file pointer
m.seek(0)

# Read some data via slice notation
print('First 10 bytes via slice:', m.read(10))

# Update content using slice notation;
# note that new content must have same size
m[6:16] = b' world'

# ... and read again using standard file methods.
m.seek(0)
print('First 10 bytes via read :', m.read(10))

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)
