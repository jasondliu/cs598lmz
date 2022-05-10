import mmap
# Test mmap.mmap()
fp = open("test_mmap.txt", "w+")
mm = mmap.mmap(fp.fileno(), 16 * 1024)
mm.write("hello world!")
mm.seek(0)
print mm.read(16 * 1024)#mmap(fp.fileno(), 16 * 1024)
mm.close()

# Test mmap.mmap(FILL_BYTE)
fp = open("test_mmap_fill.txt", "w+")
mm = mmap.mmap(fp.fileno(), 16 * 1024, mmap.ACCESS_WRITE, mmap.MAP_PRIVATE, 0, 0, 0xff)
#mm.write("hello world!")
mm.seek(0)
print mm.read(16 * 1024)
mm.close()

# Test mmap[i]
fp = open("test_mmap_map.txt", "w+")
mm = mmap.mmap(fp.fileno(), 16 * 1024)
mm.write("hello world!")
mm.seek(0)
print mm[0]
