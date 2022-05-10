import mmap
# Test mmap.mmap()
fd = os.open('/tmp/mmapfile', os.O_CREAT | os.O_RDWR)
m = mmap.mmap(fd, 10)
m.write('0123456789')
m.close()
os.close(fd)

# Test mmap.mmap() with anonymous memory mapping
m = mmap.mmap(-1, 10)
m.write('0123456789')
m.close()
# Test mmap.mmap() with anonymous memory mapping and shared memory
m = mmap.mmap(-1, 10, mmap.MAP_SHARED)
m.write('0123456789')
