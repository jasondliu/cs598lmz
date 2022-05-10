import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+b')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Print file
print m[:]

# Close file
f.close()

# Close mmap
m.close()

# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+b')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Print file
print m[:]

# Write to file
m[:] = 'Hello World!'

# Close file
f.close()

# Close mmap
m.close()

# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+b')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Print file
print m[:]

# Write to file
m[:] = 'Hello World!'

# Close file
f.close
