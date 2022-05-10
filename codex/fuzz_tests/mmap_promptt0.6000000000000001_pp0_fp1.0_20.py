import mmap
# Test mmap.mmap()

# The file must exist
f = open('/tmp/test.txt', 'w+')
f.write('Hello\n')
f.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.readline()
m.seek(0)
m.write('World\n')
m.seek(0)
print m.readline()
m.close()
f.close()

# Test mmap.mmap(fileno, length)
f = open('/tmp/test.txt', 'w+')
m = mmap.mmap(f.fileno(), 16)
m.write('Hello world!\n')
m.close()
f.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 16)
print m.readline()
m.close()
f.close()

# Test mmap.mmap(fileno, length, tagname)
f
