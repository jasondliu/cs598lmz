import mmap
# Test mmap.mmap

# Create a file
f = open('test.txt', 'w+')
f.write('Hello world!')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Get the size of the file
st_size = os.fstat(f.fileno()).st_size

# Memory-map the file
mm = mmap.mmap(f.fileno(), st_size)

# Read the content via standard file methods
print 'First 10 bytes via read :', mm.read(10)

# Read the content via slice notation
print 'First 10 bytes via slice:', mm[:10]

# Update the file content using slice notation;
# note that new content must have same size
mm[6:] = 'WORLD'

# ... and read the rest of the content
print 'Rest of the file:', mm[10:]

# Close the map
mm.close()

# Close the file
f.close()

# Test mmap.mmap

# Create a file
f = open('test.
