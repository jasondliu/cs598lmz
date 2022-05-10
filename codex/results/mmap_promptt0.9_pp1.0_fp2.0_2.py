import mmap
# Test mmap.mmap.close?
def foo():
    fd = os.open('data', os.O_RDWR)
    mm = mmap.mmap(fd, 0)
    fd.close()
    del mm


foo()
