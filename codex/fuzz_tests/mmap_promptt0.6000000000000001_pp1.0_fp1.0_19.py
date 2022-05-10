import mmap
# Test mmap.mmap.write
f = open('test.txt', 'w+')
f.write('Hello World')
f.close()

f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m[:] = 'Hello World'
m.close()
f.close()
# Test mmap.mmap.read
f = open('test.txt', 'w+')
f.write('Hello World')
f.close()

f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
data = m.read(11)
m.close()
f.close()
print(data)

"""

"""
# Test mmap.mmap.read_byte
f = open('test.txt', 'w+')
f.write('Hello World')
f.close()

f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
data = m.read_byte(11)
m.
