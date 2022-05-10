import mmap
# Test mmap.mmap

f = open('/tmp/test.txt', 'w+')
f.write('Hello world!')
f.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.readline()
m.seek(0)
m.write('Hello world!')
m.close()
f.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.readline()
m.seek(0)
m.write('Hello world!')
m.close()
f.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.readline()
m.seek(0)
m.write('Hello world!')
m.close()
f.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fil
