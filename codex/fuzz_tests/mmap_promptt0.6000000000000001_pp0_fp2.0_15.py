import mmap
# Test mmap.mmap
# with open("/data/test.txt", "r+b") as f:
#     # memory-map the file, size 0 means whole file
#     map = mmap.mmap(f.fileno(), 0)
#     # read content via standard file methods
#     print(map.readline())  # prints "Hello world!"
#     # read content via slice notation
#     print(map[:5])  # prints "Hello"
#     # update content using slice notation;
#     # note that new content must have same size
#     map[6:] = " world!\nHowdy y'all!"
#     # ... and read again using standard file methods
#     map.seek(0)
#     print(map.readline())
#     # close the map
#     map.close()
#
# with open("/data/test.txt", "r+b") as f:
#     # memory-map the file, size 0 means whole file
#     map = mmap.mmap(f.fileno(), 0)
#     # read content via standard file
