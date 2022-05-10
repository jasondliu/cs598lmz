import mmap
# Test mmap.mmap.read_byte()
print(m.read_byte())

# Test mmap.mmap.readline()
print(m.readline())

# Test mmap.mmap.read()
print(m.read(10))

# Test mmap.mmap.read_byte() again, to see if the cursor moved
print(m.read_byte())

# Test mmap.mmap.seek()
m.seek(0)
print(m.read_byte())

# Test mmap.mmap.tell()
print(m.tell())

# Test mmap.mmap.close()
m.close()

# Test mmap.mmap.find()
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(m.find(b'Python'))
m.close()

# Test mmap.mmap.rfind()
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(m.rfind(b'
