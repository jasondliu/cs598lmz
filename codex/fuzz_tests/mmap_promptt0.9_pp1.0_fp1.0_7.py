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

fd = os.open(file_name, os.O_RDWR)
f = mmap.mmap(fd, MAP_SIZE, access = mmap.ACCESS_WRITE)
# Test mmap.mmap.fromfile(self)
f.fromfile(sys.stdin, 100)
# Test mmap.mmap.write(self, bytes)
test_string = 'Python says hello to the world!'
f.write(test_string)
# Test mmap.mmap.read(self, size)
ret_val = f.read(len(test_string))
assert ret_
