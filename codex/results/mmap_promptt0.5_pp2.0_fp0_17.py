import mmap
# Test mmap.mmap
import mmap

print "Testing mmap module:"

# Open a file to use as a backing store
f = open('test.mmap', 'w+')

# Create an mmap object.
# For this example, we'll create a memory-mapped file that is 256 bytes long.
m = mmap.mmap(f.fileno(), 256, access=mmap.ACCESS_WRITE)

# Write to the mmap object.
# (This will automatically write to the file)
m.write('abcdefghijklmnop')

# Read from the mmap object.
# (This will automatically read from the file)
print m.read(16)

# Print the current position
print "Current position:", m.tell()

# Reposition to the beginning
m.seek(0)

# Read the first 16 bytes again
print m.read(16)

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap
import mmap

print "Testing mmap module:"
