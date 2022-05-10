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
