import mmap
# Test mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE)
f = open('testmmap.txt', 'w+')
f.write('abcd'*10)
f.seek(0)
m = mmap.mmap(f.fileno(), 0)
