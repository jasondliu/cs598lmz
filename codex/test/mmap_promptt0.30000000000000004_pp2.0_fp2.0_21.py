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
