import mmap
# Test mmap.mmap.resize()

# Create a file and open it for read write
f = open('resizetest.bin', 'w+')
f.write('\x00' * 10)
f.seek(0)

# Create a mmap and resize it
m = mmap.mmap(f.fileno(), 0)
m.resize(100)

# Do some operations on the mmap
m.write('\x01' * 100)
m.seek(0)
print repr(m.read(10))

# Close the mmap and file
m.close()
f.close()
