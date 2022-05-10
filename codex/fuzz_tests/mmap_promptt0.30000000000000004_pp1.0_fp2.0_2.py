import mmap
# Test mmap.mmap
# fd = os.open("/tmp/mmaptest", os.O_CREAT | os.O_RDWR)
# os.write(fd, "1234567890"*100)
# os.close(fd)
#
# fd = os.open("/tmp/mmaptest", os.O_RDWR)
# buf = mmap.mmap(fd, 0)
# print buf[0:10]
# print buf[10:20]
# print buf[0]
# buf[0] = 'J'
# print buf[0]
# buf.close()
# os.close(fd)

# Test mmap.mmap
# fd = os.open("/tmp/mmaptest", os.O_CREAT | os.O_RDWR)
# os.write(fd, "1234567890"*100)
# os.close(fd)
#
# fd = os.open("/tmp/mmaptest", os.O_RDWR)
# buf = mmap.mmap(fd, 0)
#
