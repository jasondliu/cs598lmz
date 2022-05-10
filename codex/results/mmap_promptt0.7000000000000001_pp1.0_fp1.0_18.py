import mmap
# Test mmap.mmap(fileno, length, access)
# length is (end - start)
# access is one of ACCESS_READ, ACCESS_WRITE, or ACCESS_COPY

# Create a test file
f = open('mmap_test', 'w+')

# Write bytes to the file
f.write('\x00' * 100)

# Close the file so that the mmap'ed region is valid
f.close()

# Open the file again as read-only
f = open('mmap_test', 'r')

# Create an mmap'ed region that's writeable
m = mmap.mmap(f.fileno(), 100, mmap.ACCESS_WRITE)

# Update the contents of the mmap'ed region
m[0:5] = 'Hello'

# Close the file first, then the mmap
f.close()
m.close()
