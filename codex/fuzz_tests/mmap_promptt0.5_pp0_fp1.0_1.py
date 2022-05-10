import mmap
# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')

# Write some data
f.write('01234567890123456789')

# Close the file
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read some data
print('First 10 bytes via read :', m.read(10))

# Reset the pointer
m.seek(0)

# Read some data via slice notation
print('First 10 bytes via slice:', m[:10])

# Update data in the memory-mapped file
m[0:11] = b'Hello World'
m.close()

# Verify that changes were made
f = open('test.txt', 'r')
print(f.read(11))
f.close()

# Cleanup
os.unlink('test.txt')

# Test mmap.mmap()


