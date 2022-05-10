import mmap
# Test mmap.mmap
#f = open('file.txt', 'r')
#m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
#print m.readline()
#print m.readline()
#print m.readline()
#m.seek(0)
#print m.readline()
#print m.readline()
#m.close()

# Test mmap.mmap with write
#import mmap
#f = open('file.txt', 'r+')
#m = mmap.mmap(f.fileno(), 0)
#print m.readline()
#print m.readline()
#m.seek(0)
#m.write('abcde')
#m.seek(0)
#print m.readline()

# Test mmap.mmap with offset
#import mmap
#f = open('file.txt', 'r')
#m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ, offset=3)
#print m.
