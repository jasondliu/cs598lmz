import mmap
# Test mmap.mmap()
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.write('hello world')
m.seek(0)
print(m.readline())
m.close()
f.close()

# Test mmap.mmap() with fileno()
f = open('test.txt', 'w+')
f.write('hello world')
m = mmap.mmap(f.fileno(), 0)
print(m.readline())
m.close()
f.close()

# Test mmap.mmap() with length
f = open('test.txt', 'w+')
f.write('hello world')
m = mmap.mmap(f.fileno(), 5)
print(m.readline())
m.close()
f.close()

# Test mmap.mmap() with offset
f = open('test.txt', 'w+')
f.write('hello world')
m = mmap.mmap(f.fileno(), 5, 1)
print(m.
