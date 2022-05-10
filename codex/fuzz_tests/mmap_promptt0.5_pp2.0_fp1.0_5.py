import mmap
# Test mmap.mmap
# open a file
f = open('/tmp/test.txt', 'r+')
# memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print mm.readline()  # prints "Hello Python!"
mm.seek(0)  # rewind
# write to the file
mm.write('Hello World!')
mm.close()

# Test mmap.mmap(-1, size)
# memory-map an anonymous file
size = 100
m = mmap.mmap(-1, size)
# write some data to the file
m.write('\x00' * size)
m.seek(0)  # rewind
# read content via standard file methods
print m.readline()  # prints "\x00" * 100
m.close()

# Test mmap.mmap(fileno, length, tagname, access=ACCESS_DEFAULT[, offset])
# open a file
f = open('/tmp/test.txt', 'r+')
# memory
