import mmap
# Test mmap.mmap

# Open file
f = open('../data/test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

# Print file as a string
print 'Print file as a string: ', m.readline()

# Close mmap
m.close()

# Close file
f.close()

# Open file
f = open('../data/test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

# Print file as a string
print 'Print file as a string: ', m.readline()

# Close mmap
m.close()

# Close file
f.close()
 
# Open file
f = open('../data/test.txt', 'r+')

# Create mmap
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

# Print
