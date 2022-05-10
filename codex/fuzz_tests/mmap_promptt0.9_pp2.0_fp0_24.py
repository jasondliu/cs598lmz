import mmap
# Test mmap.mmap
fh = open('mmapfile', 'w+')
fh.write('01234567890123456789')

m = mmap.mmap(fh.fileno(), 0)
print m[0], m[9]
m.seek(0)
m.write('@')
m.close()
fh.close()

# Test os.ftruncate
fh = open('ftruncate', 'w+')
fh.write('01234567890123456789')
fh.close()
fh = open('ftruncate', 'r+')
t = fh.read(5)
fh.seek(0)
fh.write('z' * 5)
os.ftruncate(fh.fileno(), 11)
fh.seek(0)
t += fh.read()
fh.close()
print t

try:
    os.ftruncate(fh.fileno(), 3)
except IOError, e:
    print e
    
# test os
