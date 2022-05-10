import mmap
# Test mmap.mmap
m = mmap.mmap(0, 1024)
m.write("Hello, world!")
print m.read()
m.close()

'''
import mmap
import struct

# Open memory-mapped file
with open("lorem.txt", "r+b") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print mm.readline()  # prints "Hello Python!"
    # Update content using slice notation;
    # note that new content must have same size
    mm[0:17] = "Hello, Python!"
    mm.seek(0)  # rewind
    print mm.readline()  # prints "Hello Python!"
    # close the map
    mm.close()

'''

'''
print "this is a test"

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print "
