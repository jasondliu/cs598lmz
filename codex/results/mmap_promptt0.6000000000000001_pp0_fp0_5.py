import mmap
# Test mmap.mmap
m = mmap.mmap(-1, 13)
m.write('Hello Python!')
m.seek(0)
print m.read(13)

# Test mmap.mmap with fileno
f = open('/tmp/mmaptest', 'w+')
f.write('Hello World!')
f.flush()
m = mmap.mmap(f.fileno(), 13)
m.seek(0)
print m.read(13)

# Test mmap.mmap with offset
m = mmap.mmap(f.fileno(), 13, offset=6)
m.seek(0)
print m.read(13)

# Test mmap.mmap with access=mmap.ACCESS_WRITE
m = mmap.mmap(f.fileno(), 13, access=mmap.ACCESS_WRITE)
m.seek(0)
print m.read(13)
m.write('Hello Python!')
m.seek(0)
print m.read(13)

# Test mmap.mmap with access=mm
