import mmap
# Test mmap.mmap.find and index
fd = os.open('tmpfile2', os.O_RDWR)
m = mmap.mmap(fd, length=1024, tagname="test")
m.find(b'A')
m.index(b'A')
