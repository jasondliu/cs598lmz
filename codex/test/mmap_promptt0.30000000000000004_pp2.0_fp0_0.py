import mmap
# Test mmap.mmap
m = mmap.mmap(-1, 1024)
m.write(b'Hello Python!')
m.seek(0)
print(m.read(11))

# Test mmap.mmap(fileno, length)
m = mmap.mmap(f.fileno(), 1024)
m.write(b'Hello Python!')
m.seek(0)
print(m.read(11))

# Test mmap.mmap(fileno, length, tagname)
m = mmap.mmap(f.fileno(), 1024, tagname='test')
m.write(b'Hello Python!')
m.seek(0)
print(m.read(11))

# Test mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE)
m = mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_WRITE)
m.write(b'Hello Python!')
m.seek(0)
print(m.read(11))

