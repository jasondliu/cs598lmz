import mmap
# Test mmap.mmap()

# Create file
with open('lorem.txt', 'w') as f:
    f.write('Hello world')

# Open file
f = open('lorem.txt', 'r+')
# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# Read content via standard file methods
print m.readline()

# Update content using slice notation;
# note that new content must have same size
m[6:] = 'WORLD'
# ... and read again using standard file methods
m.seek(0)
print m.readline()

# Close the map
m.close()
# Close the file
f.close()
 
# Open file
f = open('lorem.txt', 'r+')
# Memory-map the file, size 0 means whole file, read-only
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# Read content via standard file methods
print m.readline()

# Try to write to m
m
