import mmap
# Test mmap.mmap()
f = open('text.txt', 'r+')
mapf = mmap.mmap(f.fileno(), 0)
print repr(mapf.read(3))
mapf.seek(0)
mapf.write('xyz')
mapf.write(',')
mapf.write('xyz')
mapf.flush()
f.close()
mapf.close()

# Test mmap.mmap(fileno, size...)
f = open('text.txt', 'r+')
mapf = mmap.mmap(f.fileno(), 2)
print repr(mapf.read(3))
mapf.seek(0)
mapf.write('xyz')
mapf.flush()
f.seek(0)
print f.read(3)
f.close()
mapf.close()

# Test mmap.mmap(fileno, length, tagname)
f = open('text.txt', 'r+')
mapf = mmap.mmap(f.fileno(), 2, 'test')
print repr(mapf
