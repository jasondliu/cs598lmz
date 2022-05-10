import mmap
# Test mmap.mmap()

# Create a file and open it for writing
f = open('test.dat', 'w+')
# Write a bunch of data to the file
for i in range(100):
    f.write('%d\n' % i)
# Close the file
f.close()

# Open the file for reading
f = open('test.dat', 'r+')
# Map the file into memory
m = mmap.mmap(f.fileno(), 0)
# Read the first 10 bytes from the file
