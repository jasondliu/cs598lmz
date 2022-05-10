import mmap
# Test mmap.mmap(0, 10000, "COM1", access=mmap.ACCESS_WRITE)
mapping = struct.pack("=B", 0x41)
print(mapping)
fp = open("COM1")
m = mmap.mmap(fp.fileno(), 10000, mmap.ACCESS_WRITE)
m.write(mapping)
m.close()
