import mmap
# Test mmap.mmap object
mem = mmap.mmap(-1, 10)
mem.write("1234567890")
del mem
mem = mmap.mmap(-1,10)
buf = ''
while mem.tell() < 10:
	buf += mem.readline()
del mem
