import mmap
# Test mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE)
f = open('testmmap.txt', 'w+')
f.write('abcd'*10)
f.seek(0)
m = mmap.mmap(f.fileno(), 0)
print m.read(4)
#print m.read(5)
## Traceback (most recent call last):
##   File "testmmap.py", line 9, in ?
##     print m.read(5)
## ValueError: mmap offset is greater than file size
#m.close()
#f.close()
#m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
#print m.read(4)
#print m.read(5)
#m.close()
# Test mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE)
#f = open('testmmap.txt', 'w+')
#f.write('abcd'*10)
#f.seek(0
