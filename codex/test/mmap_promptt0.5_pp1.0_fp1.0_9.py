import mmap
# Test mmap.mmap

# Open a file
f = open('test.txt', 'r+b')

# Memory-map the file, size 0 means whole file
#mm = mmap.mmap(f.fileno(), 0)
mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read content via standard file methods
print(f.readline())

# Read content via mmap
mm.seek(0)
print(mm.readline())

# Update content using mmap
mm.seek(0)
mm.write(b'Hello world!')
mm.seek(0)
print(mm.readline())

# Close the map
mm.close()
f.close()

# Reopen the file and check content
f = open('test.txt', 'r+b')
print(f.readline())
f.close()

# Clean up
os.remove('test.txt')

# Test mmap.mmap

# Open a file
