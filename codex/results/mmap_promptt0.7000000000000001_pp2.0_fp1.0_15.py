import mmap
# Test mmap.mmap() for a read-only file
f = open("a.txt", "r+")
f.write("This is a test")
f.close()
f = open("a.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
print "Before", m.readline()

m.seek(0) # rewind
# write() raises a TypeError when the mmap
# is read-only
try:
    m.write("r")
except TypeError:
    print "TypeError"
finally:
    m.close()

# Test mmap.mmap() for a writeable file
f = open("a.txt", "r+")
m = mmap.mmap(f.fileno(), 0)

print "Before", m.readline()
m.seek(0) # rewind
m.write("r")
m.seek(0) # rewind
print "After", m.readline()

m.close()

# Test mmap.mmap() for a writeable file
f = open("a
