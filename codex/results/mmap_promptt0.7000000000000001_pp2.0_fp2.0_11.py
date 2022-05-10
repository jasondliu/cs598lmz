import mmap
# Test mmap.mmap()
file_ = open('testfile', 'w+')
file_.write(b'abcd' * 1000000)
file_.close()
# Open file
file_ = open('testfile', 'r+')
# Memory-map the file, size 0 means whole file
mm = mmap.mmap(file_.fileno(), 0)
# Read content via standard file methods
print(mm.readline())  # prints "b'abcdabcdabcd..."
# Update content using slice notation;
# note that new content must have same size
mm[5:10] = b'xxxxx'
# ... and read again using standard file methods
mm.seek(0)  # rewind
print(mm.readline())  # prints b'abxxxxxabcd...'
# close the map
mm.close()
# close the file
file_.close()

# Test mmap.mmap(-1, ...)
file_ = open('testfile', 'w+')
file_.write(b'abcd' * 1000000)
file_.close()
# Open file
file_ = open
