import mmap
# Test mmap.mmap()
f = open(os.path.join(os.getcwd(), 'test.txt'), 'r+')
m = mmap.mmap(f.fileno(), 0)
m.write('0123456789abcdef')
m.seek(0)
print m.read(10)
m.seek(3)
print m.read(1)
m.close()
f.close()

# Test mmap.mmap() with size
f = open(os.path.join(os.getcwd(), 'test.txt'), 'r+')
m = mmap.mmap(f.fileno(), 16)
m.write('0123456789abcdef')
m.seek(0)
print m.read(10)
m.seek(3)
print m.read(1)
m.close()
f.close()

# Test mmap.mmap() with access=mmap.ACCESS_READ
f = open(os.path.join(os.getcwd(), 'test.txt'), 'r+')
m = mmap.
