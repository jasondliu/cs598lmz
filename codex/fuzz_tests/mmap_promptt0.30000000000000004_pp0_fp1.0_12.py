import mmap
# Test mmap.mmap(0, 1, "sharedmem", mmap.ACCESS_READ)

# This is a simple example of how to use the mmap module to
# create a memory-mapped file.

# Create a memory-map to an existing file.  The size of the
# file must be known ahead of time.
f = open('lorem.txt', 'r+b')
mm = mmap.mmap(f.fileno(), 0)
# Read contents...
print mm.readline()  # prints "Lorem ipsum dolor sit amet, consectetuer..."
# Close the map
mm.close()
# Close the underlying file
f.close()
