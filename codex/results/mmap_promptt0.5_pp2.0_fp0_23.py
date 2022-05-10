import mmap
# Test mmap.mmap
# https://docs.python.org/3/library/mmap.html

# Example 1
# f = open('lorem.txt', 'r+b')
# # memory-map the file, size 0 means whole file
# map = mmap.mmap(f.fileno(), 0)
# # read content via standard file methods
# print(map.readline())  # prints "Hello Python!\n"
# # read content via slice notation
# print(map[:5])  # prints "Hello"
# # update content using slice notation;
# # note that new content must have same size
# map[6:] = b'world'
# # ... and read again using standard file methods
# map.seek(0)
# print(map.readline())  # prints "Hello world!"
# # close the map
# map.close()
# # close the file
# f.close()

# Example 2
# f = open('lorem.txt', 'r+b')
# # memory-map the file, size 0 means whole file
# map = mmap.mmap
