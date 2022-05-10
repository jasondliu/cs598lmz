import mmap
# Test mmap.mmap
m = mmap.mmap(0, 32, "test")
m.write("1234567890abcdefghijklmnopqrstuv")
m.seek(0)
print m.read(16)
m.seek(16)
print m.read(16)
print m.tell()
print m.read(16)
m.seek(0)
print m.read(16)
m.close()
# Test mmap.mmap() with offset
m = mmap.mmap(0, 32, "test")
m.write("1234567890abcdefghijklmnopqrstuv")
m.seek(0)
print m.read(16)
m.seek(16)
print m.read(16)
print m.tell()
print m.read(16)
m.seek(0)
print m.read(16)
m.close()
# Test mmap.mmap() with offset
m = mmap.mmap(0, 32, "test")
m.write("1234567890abcdefghijklmn
