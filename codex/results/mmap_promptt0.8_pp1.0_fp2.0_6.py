import mmap
# Test mmap.mmap(0,1).read_byte()
m = mmap.mmap(0, 1)
print(m.read_byte())
# Test mmap.mmap(0,0).read_byte()
try:
    m = mmap.mmap(0, 0)
except ValueError:
    pass
else:
    print(m.read_byte())
