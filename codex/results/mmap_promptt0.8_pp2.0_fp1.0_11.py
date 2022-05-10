import mmap
# Test mmap.mmap()
# https://docs.python.org/2/library/mmap.html

f = open("foo.txt", "w+")
f.write("Hello Python!\nWow, it\'s very interesting.\n")
f.close()

f = open("foo.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
print m.readline()

m.seek(0) # rewind
print m.readline()

m.seek(0) # rewind
line = m.readline()
print m.tell()

m.seek(0, 2) # report file size
print m.tell()

m.seek(11)
print m.read(1)

m.close()
