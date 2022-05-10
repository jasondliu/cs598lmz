import mmap
# Test mmap.mmap()
# O_RDWR: Open for reading and writing.
# m = mmap.mmap(-1, 1024, "MySharedMemory", mmap.ACCESS_WRITE)
# Test mmap.mmap() without flags
m = mmap.mmap(-1, 1024, "MySharedMemory")
# print m[:10]
# print m[2:5]
# print m[0]
# print m[0:1]
# print m.size()
# print m.tell()
# print m.seek(0)
# print m.read(1)
# print m.read_byte()
# print m.readline()
# print m.readline(8)
# print m.write(b'0123456789abcdef')
# print m.write_byte(65)
# print m.write_byte(66)
# print m.write_byte(67)
# m.seek(0)
# print m.read(16)
# print m.flush()
# print m.move(0, 16, 8)
# print
