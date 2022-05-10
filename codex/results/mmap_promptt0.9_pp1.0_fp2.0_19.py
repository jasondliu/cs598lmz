import mmap
# Test mmap.mmap
a = mmap.mmap(0, 1024, "MyMap") 
a.write("characters")
print a.read(8)
a.seek(0)
v = a.read_byte()
