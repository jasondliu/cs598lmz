import mmap
# Test mmap.mmap(f.fileno(), 0)
# https://docs.python.org/3.6/library/mmap.html
# Creates a memory-map to an existing file. The size of the mapped region is equal to the length of the file.
f = open("test", "w+")
size = mmap.PAGESIZE
f.write('\0' * size)
m = mmap.mmap(f.fileno(), size)
# print(m.read(4))
# Write 1024 bytes data
# bytearray(size)
m.write(bytearray(size))
# m.write_byte('\0')
# print(m.read(4))
m.close()
f.close()
# m = mmap.mmap(f.fileno(), 0)
# print(m[:])
# print('f.fileno()', f.fileno())
# print(m.readline())
# m.close()
# f.close()

# Test mmap.mmap(-1, size, flags[, prot[, access[,
