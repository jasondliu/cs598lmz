import mmap
# Test mmap.mmap
# mm = mmap.mmap(0, 1024, "MySharedMemory", mmap.ACCESS_WRITE)
# mm.seek(0)
# mm.write("Hello Python!")
# mm.close()

# Test mmap.mmap(fileno, length, tagname=None, access=ACCESS_DEFAULT, offset=0)
# f = open("testfile.txt", "r+")
# mm = mmap.mmap(f.fileno(), 0)
# mm.write("Hello Python!")
# mm.close()

# Test mmap.mmap(fileno, length, tagname=None, access=ACCESS_DEFAULT, offset=0)
f = open("testfile.txt", "w+")
f.write("Hello Python!")
f.close()
f = open("testfile.txt", "r+")
mm = mmap.mmap(f.fileno(), 0)
print mm.readline()
mm.close()
