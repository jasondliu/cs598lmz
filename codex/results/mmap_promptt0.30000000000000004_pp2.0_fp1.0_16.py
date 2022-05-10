import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file as string
print 'First 10 bytes via read :', m.read(10)

# Close the map
m.close()

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via slice notation
print 'First 10 bytes via slice:', m[:10]

# Close the map
m.close()

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via buffer interface
print 'First 10 bytes via buffer:', buffer(m, 0, 10)

# Close the map
m.close()

# Close the file

