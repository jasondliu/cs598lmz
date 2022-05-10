import mmap
# Test mmap.mmap.resize()

# Create a file and memory map it.
with open('resize.dat', 'wb') as f:
    f.write(b'0' * 10)

f = open('resize.dat', 'rb+')
m = mmap.mmap(f.fileno(), 0)

# Resize the memory map.
m.resize(20)

# Verify the file is now larger.
assert os.path.getsize('resize.dat') == 20

# Write some data to the memory map.
m[10:] = b'1' * 10

# Verify the data was written to the file.
assert m.read(20) == b'0' * 10 + b'1' * 10

# Clean up.
m.close()
f.close()
os.unlink('resize.dat')
