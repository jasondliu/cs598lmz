import mmap
# Test mmap.mmap

f = open('/tmp/test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.seek(5)
print m.read(1)
m.seek(4)
m.write('4')
m.seek(6)
m.write('6')
m.close()
f.close()

print open('/tmp/test.txt').read()

# Test mmap.mmap(-1, ...)

f = open('/tmp/test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
m.seek(5)
print m.read(1)
m.close()
f.close()

print
