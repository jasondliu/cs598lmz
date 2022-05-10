import mmap
# Test mmap.mmap for reading
f = open('D:/temp/test.txt', 'r+')
# memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print(m.readline())
# read content via slice notation
print(m[:5])
# update content using slice notation;
# note that new content must have same size
#m[6:] = 'world'
# ... and read again using standard file methods
m.seek(0)
print(m.readline())
# close the map
m.close()

# Test mmap.mmap for writing
f = open('D:/temp/test.txt', 'r+')
# memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print(m.readline())
# read content via slice notation
print(m[:5])
# update content using slice notation;
# note that new content must have same size
