import mmap
# Test mmap.mmap()
print('Test mmap.mmap():')
f = open('lorem.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(len(m))
print(m[0:25])
m.close()
f.close()

# Test mmap.mmap() with offset
print('Test mmap.mmap() with offset:')
f = open('lorem.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(len(m))
print(m[10:10+25])
m.close()
f.close()


# Test mmap.mmap() with size
print('Test mmap.mmap() with size:')
f = open('lorem.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(len(m))
print(m[0:50])
m.close
