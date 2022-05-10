import mmap
# Test mmap.mmap(offset)

# Create file
try:
    os.unlink("test.dat")
except OSError:
    pass

f = open("test.dat", "w+")
f.write("0123456789")
f.flush()

# Map file with offset
m = mmap.mmap(f.fileno(), 10, offset=5)

# Check content and size
