import mmap
# Test mmap.mmap()
# https://docs.python.org/2/library/mmap.html

f = open("test.txt", "r+")
# size = os.path.getsize("test.txt")
# print size

m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
# print len(m)
# print m.readline()
m.seek(0)
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
m.write("replace the value")
