import mmap
# Test mmap.mmap()
# fd = os.open('/tmp/mmap_test', os.O_CREAT|os.O_RDWR)
# os.write(fd, b'Hello world!')
# m = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_WRITE)
# print(m[6:12])
#
# m.seek(6)
# m.write_byte(b'y')
# m.close()
# os.close(fd)
#
#
#
#
#
# # Test mmap.mmap().write()
# fd = os.open('/tmp/mmap_test', os.O_CREAT|os.O_RDWR)
# os.write(fd, b'Hello world!')
# m = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_WRITE)
#
# m.write(b'yyy')
# m.seek(0)
# m.write(b'1234')
