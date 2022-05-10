import mmap
# Test mmap.mmap function

# open a file for updating
# (gives us a file handle to work with)
f = open('lorem.txt', 'r+')

# memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# read content via standard file methods
print(m.readline())  # prints "Hello Python!\n"

# read content via slice notation
print(m[:5])  # prints "Hello"

# update content using slice notation;
# note that new content must have same size
m[6:] = 'world!'

# ... and read again using standard file methods
m.seek(0)  # rewind
print(m.readline())  # prints "Hello world!"

# close the map
m.close()

# close the file
f.close()

# test mmap.mmap function

# open file
f = open('lorem.txt', 'r+')
