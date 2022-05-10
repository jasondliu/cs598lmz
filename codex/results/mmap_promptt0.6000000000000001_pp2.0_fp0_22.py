import mmap
# Test mmap.mmap()
f = open("/proc/self/maps", "r+")
m = mmap.mmap(f.fileno(), 0)
m.readline() # Returns first line
m.seek(0,0) # Move to beginning of file

# Test mmap.mmap() with custom size
m = mmap.mmap(-1, 1024)
m.write("Hello World!")
m.seek(0)
m.read(11)
m.close()

# Test mmap.mmap() with custom offset
f = open("/proc/self/maps", "r+")
m = mmap.mmap(f.fileno(), 1024, offset=1024)
m.readline() # Returns second line
m.close()

# Test mmap.mmap() with custom offset and size
f = open("/proc/self/maps", "r+")
m = mmap.mmap(f.fileno(), 1024, 1024, mmap.MAP_SHARED, mmap.PROT_READ)
m.readline() # Returns second line
m.
