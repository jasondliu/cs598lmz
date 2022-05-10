import mmap
# Test mmap.mmap()
# f = open("/tmp/test.txt", "w+")
# f.write("This is a test")
# f.close()
#
# f = open("/tmp/test.txt", "r+")
# m = mmap.mmap(f.fileno(), 0)
# print m.readline()
# m.seek(0) # rewind
# m.write("This is another test")
# m.close()
# f.close()

# Test mmap.mmap() with access=mmap.ACCESS_WRITE
# f = open("/tmp/test.txt", "w+")
# f.write("This is a test")
# f.close()
#
# f = open("/tmp/test.txt", "r+")
# m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
# print m.readline()
# m.seek(0) # rewind
# m.write("This is another test")
# m.close()
# f.
