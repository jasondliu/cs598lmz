import mmap
# Test mmap.mmap()
f = open("C:\\Users\\peng\\Desktop\\test.txt", "r")
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print (m.readline())
print (m.readline())
print (m.readline())
m.close()

# Test mmap.mmap(length)
m = mmap.mmap(-1, 200)
print (len(m))
print (m[0:10])
m.close()

# Test mmap.mmap(fileno, length)
f = open("C:\\Users\\peng\\Desktop\\test.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
print (m.readline())
print (m.readline())
print (m.readline())
m.close()

# Test mmap.mmap(fileno, length, tagname)
m = mmap.mmap(-1, 200, "MyTag")
print (len(m))
print (m[0
