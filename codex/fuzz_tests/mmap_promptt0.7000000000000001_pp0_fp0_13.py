import mmap
# Test mmap.mmap() function
f = open("/tmp/mmap_test.txt", "w+")
# mmap.mmap(fileno, length, tagname=None, access=mmap.ACCESS_DEFAULT, offset=0)
m = mmap.mmap(f.fileno(), 0)
m.write("Hello World")
m.seek(0)
print m.readline()
m.close()
f.close()
