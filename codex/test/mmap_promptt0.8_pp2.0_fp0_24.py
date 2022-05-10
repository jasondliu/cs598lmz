import mmap
# Test mmap.mmap
m = mmap.mmap(0, 1024, "Hello", mmap.ACCESS_READ)
m[:5]

# Test mmap.mmap.read_byte
m.seek(0)
m.read_byte()

# Test mmap.mmap.readline
m.seek(0)
m.readline()

# Test mmap.mmap.read
m.seek(0)
m.read(256)

# Test mmap.mmap.write
m.seek(0)
m.write("Goodbye")

# Test mmap.mmap.close
m.close()
print('pass')
