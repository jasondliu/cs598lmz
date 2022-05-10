import mmap
# Test mmap.mmap()

fp = open("/tmp/mmap.bin", "wb")
#fp.write(b'\0' * mmap.PAGESIZE)
fp.close()

fp = open("/tmp/mmap.bin", "r+b")
m = mmap.mmap(fp.fileno(), mmap.PAGESIZE)
m[0:3] = b'\x00\x01\x02'
m.seek(0)
print(m.read(3))
m.close()
fp.close()

# Test mmap.mmap(fileno, 0)

fp = open("/tmp/mmap.bin", "wb")
fp.write(b'\0' * mmap.PAGESIZE)
fp.close()

fp = open("/tmp/mmap.bin", "r+b")
m = mmap.mmap(fp.fileno(), 0)
m[0:3] = b'\x00\x01\x02'
m.seek(0)
print(m.read(3))
