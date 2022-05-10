import mmap
# Test mmap.mmap class

f = file("data")
m = mmap.mmap(f.fileno(), 0, mmap.ACCESS_READ)
print m[0:10]
print m.tell(), m.readline(), m.readline()
m.seek(0)
print m.readline(), m.readline()
m.seek(0)
for line in iter(m.readline, ""):
    print line,
m.close()
f.close()
