import mmap
# Test mmap.mmap()
fd = os.open(os.path.join(os.getcwd(), "test.txt"), os.O_RDWR)
m = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)
m[0:10] = "0123456789"
m.close()
os.close(fd)
# Test mmap.mmap() with size
fd = os.open(os.path.join(os.getcwd(), "test.txt"), os.O_RDWR)
m = mmap.mmap(fd, 10, access=mmap.ACCESS_WRITE)
m[0:10] = "0123456789"
m.close()
os.close(fd)
# Test mmap.mmap() with offset
fd = os.open(os.path.join(os.getcwd(), "test.txt"), os.O_RDWR)
m = mmap.mmap(fd, 10, offset=0, access=mmap.ACCESS_WRITE)
m[0:10] = "
