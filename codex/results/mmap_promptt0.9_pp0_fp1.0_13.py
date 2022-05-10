import mmap
# Test mmap.mmap class
data = "This is a test string for mmap module."

f = open("mmap_test", "w+")
f.write(data)
f.close()

f = open("mmap_test", "r+")
m = mmap.mmap(f.fileno(), 0)

print "mmap_test file before writing : ",
print m.readline()

print "Length of data : ",
print len(data)
m[17:29] = "module."

print "mmap_test file after writing : ",
m.seek(0)
print m.readline()

print "Current position : ",
print m.tell()

m.close()
f.close()
# Test mmap.mmap class
data = "This is a test string for mmap module."

f = open("mmap_test", "w+")
f.write(data)
f.close()

f = open("mmap_test", "r+")
m = mmap.mmap(f.fileno(), 0)

print
