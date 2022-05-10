import mmap
# Test mmap.mmap()

# Create a file.
f = open('test.dat', 'w+')

# Create the mmap object.
m = mmap.mmap(f.fileno(), 0)

# Write to the file.
m.write('Hello World')

# Read from the file.
m.seek(0)
