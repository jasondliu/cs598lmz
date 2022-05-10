import mmap
# Test mmap.mmap
f = open('/home/zhaokui/Downloads/test.txt', 'r+')

m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
m.write(b'0123456789abcdef')
m.seek(5)
print(m.read(1))
m.close()
