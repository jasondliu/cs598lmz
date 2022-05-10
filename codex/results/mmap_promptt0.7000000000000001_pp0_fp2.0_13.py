import mmap
# Test mmap.mmap()

# import mmap

# # Create a memory-map to a file, size 0 means whole file
# mm = mmap.mmap(f.fileno(), 0)
# # read content via standard file methods
# print mm.readline(); print
# print mm.readline(); print
# # read content via slice notation
# print mm[:5]; print
# print mm[4:8]; print
# # update content using slice notation;
# # note that new content must have same size
# mm[4:8] = 'xxxx'; print
# mm.seek(0)
# print mm.readline()
# # close the map
# mm.close()
# # Open the file for reading.
# # f = open('lorem.txt', 'r')
# f = open('test_file.txt', 'r')

# # Create a memory-map to the file.
# m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# # Read some data.
# m.read(100)
# #
