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
print "Content ==", repr(m.read(10))
print "Size ==", m.size()

# Modify content
m[:] = "abcde"

# Compare file content
f.seek(0)
print "File content ==", repr(f.read(10))

# Clean up
m.close()
f.close()
os.unlink("test.dat")
