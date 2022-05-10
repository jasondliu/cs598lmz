import mmap
# Test mmap.mmap
#
# Open a file
#
# f = open("test.txt", "r+")
#
# # mmap the file
# m = mmap.mmap(f.fileno(), 0)
#
# # read content via standard file methods
# print m.readline()
#
# # read content via slice notation
# print m[:5]
#
# # update content using slice notation;
# # note that new content must have same size
# m[6:] = " world!\n"
#
# # ... and read again using standard file methods
# m.seek(0)
# print m.readline()
#
# # close the map
# m.close()
#
# # close the file
# f.close()

# Test mmap.mmap.resize
#
# f = open("test.txt", "r+")
#
# # Add content to the file
# f.write("1234567890"*1000)
# f.flush()
#
# # mmap the file
# m = mmap.mmap(
