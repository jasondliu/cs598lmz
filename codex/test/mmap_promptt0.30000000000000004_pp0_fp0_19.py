import mmap
# Test mmap.mmap()
# https://docs.python.org/3/library/mmap.html

# Create a file and memory map it
# f = open('test.txt', 'w+')
# f.write('Hello World')
# f.close()

# f = open('test.txt', 'r+')
# m = mmap.mmap(f.fileno(), 0)
# print(m.readline())
# m.seek(0)
# m.write('Hello World')
# m.seek(0)
# print(m.readline())
# m.close()
# f.close()

# Create a file and memory map it
f = open('test.txt', 'w+')
f.write('Hello World')
f.close()

f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print(m.readline())
m.seek(0)
m.write('Hello World')
m.seek(0)
print(m.readline())
m.close()

