import mmap
# Test mmap.mmap

mmap.mmap()
 
# file = open('testfile.txt', 'r+')

# # memory-map the file, size 0 means whole file
# mm = mmap.mmap(file.fileno(), 0)

# # read content via standard file methods
# print mm.readline()

# # read content via slice notation
# print mm[:5]

# # update content using slice notation;
# # note that new content must have same size
# mm[6:] = 'world'

# # close the map
# mm.close()

# # ...or access outer file methods
# print mm.size()

# # file.close()
