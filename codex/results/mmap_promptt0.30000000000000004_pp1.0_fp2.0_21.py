import mmap
# Test mmap.mmap

f = open('test.txt', 'r+')
# memory-map the file, size 0 means whole file
map = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print map.readline()  # prints "Hello Python!"
# read content via slice notation
print map[:5]  # prints "Hello"
# update content using slice notation;
# note that new content must have same size
map[6:] = 'world'
# ... and read again using standard file methods
map.seek(0)
print map.readline()  # prints "Hello world!"
# close the map
map.close()
# close the file
f.close()

# Test mmap.mmap

f = open('test.txt', 'r+')
# memory-map the file, size 0 means whole file
map = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print map.readline()  # prints "Hello Python!"
# read content via slice notation
print map[:5]  # prints "
