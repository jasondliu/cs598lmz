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
