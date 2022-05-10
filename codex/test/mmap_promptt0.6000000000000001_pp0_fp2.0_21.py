import mmap
# Test mmap.mmap(0,1)

f = open("test.txt", "rb")
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print (m[0])
m.close()
f.close()
