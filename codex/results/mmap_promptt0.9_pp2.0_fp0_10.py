import mmap
# Test mmap.mmap method on Ubuntu.

# Open a file.
f = open("D:/tmp/pm.pdf", 'r')

# Get size of file.
size = os.path.getsize("D:/tmp/pm.pdf")

# Create mmap object.
m = memoryview(mmap.mmap(f.fileno(), size, access=mmap.ACCESS_READ) )

# Print data.
# print m.tobytes()
print m.tobytes()[100:120]
