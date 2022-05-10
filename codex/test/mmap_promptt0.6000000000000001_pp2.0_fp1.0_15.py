import mmap
# Test mmap.mmap()

# Open file
f = open('/tmp/test', 'w+')

# Add a few lines to the file
f.write('Hello Python!\n')
f.write('Bye Python!\n')

# Close the file
f.close()

# Open the file for reading
f = open('/tmp/test', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())
print(m.readline())

# Read from position 0
m.seek(0)
print(m.read(11))

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file
f = open('/tmp/test', 'w+')

# Add a few lines to the file
f.write('Hello Python!\n')
f.write('Bye Python!\n')

# Close the file
f.close()
