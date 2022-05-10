import mmap
# Test mmap.mmap.read():
m = mmap.mmap(0, 10)
m.write(b"Hello")
print(m.read())
# Test mmap.mmap.read_byte():
# This test requires that there is already a byte present in the mmap.
b = m.read_byte()
print(b)
# Test mmap.mmap.readline():
m.write(b" line 1\n")
m.write(b" line 2\n")
m.write(b"line 3\n")
print(m.readline())
print(m.readline())
print(m.readline())
# Test mmap.mmap.seek():
m.seek(0)
print(m.readline())
m.seek(6)
print(m.readline())
# Test mmap.mmap.size():
print(m.size())
# Test mmap.mmap.tell():
print(m.tell())
