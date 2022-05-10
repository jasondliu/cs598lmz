import mmap
# Test mmap.mmap.fromfile(self)
# Test mmap.mmap.write(self, bytes)
# Test mmap.mmap.read(self, size)
# Test mmap.mmap.seek(self, offset)
# Test mmap.mmap.tell(self)
# Test mmap.mmap.close(self)


file_name = 'test.mmap_fromfile.txt'
mode = mmap.ACCESS_WRITE
MAP_SIZE = 100000

