import mmap
# Test mmap.mmap
# fd = os.open('/tmp/test.txt', os.O_RDWR)
# buf = mmap.mmap(fd, 0)
# buf[:] = 'This is a test string'
# buf.close()
# os.close(fd)

# Test mmap.mmap(fileno, length, tagname, access=ACCESS_DEFAULT, offset=0)
# fd = os.open('/tmp/test.txt', os.O_RDWR)
# buf = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)
# buf[0:13] = 'Hello Python!'
# buf.close()
# os.close(fd)

# Test mmap.mmap(fileno, length, tagname, access=ACCESS_DEFAULT, offset=0)
# fd = os.open('/tmp/test.txt', os.O_RDWR)
# buf = mmap.mmap(fd, mmap.PAGESIZE, mmap
