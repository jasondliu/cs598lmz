import mmap
# Test mmap.mmap()

f = open('test.txt', 'r+b')

# memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print(m.readline())  # prints "Hello Python!\n"

# read content via slice notation
print(m[:5])  # prints "Hello"

# update content using slice notation;
# note that new content must have same size
m[6:] = 'world!\n'

# ... and read again using standard file methods
m.seek(0)
print(m.readline())  # prints "Hello world!\n"

# close the map
m.close()

# close the file
f.close()

# Test mmap.mmap()

f = open('test.txt', 'r+b')

# memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print(m.readline()) 
