import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print m.readline()

# Update content using slice notation
# Note: new content must be same size
m[0:11] = 'Hello World'

# Close the map
m.close()

# Close the file
f.close()

# Open file for reading
f = open('test.txt', 'r')

# Print modified content
print f.readline()

# Close file
f.close()

# Open file for writing
f = open('test.txt', 'w')

# Write new content
f.write('Hello World')

# Close file
f.close()

# Open file for reading
f = open('test.txt', 'r')

# Print new content
print f.readline()

# Close file
f.close()

# Open file for writing
f = open('test.txt', 'w
