import mmap
# Test mmap.mmap()

# Open a file for writing.
# fd = os.open('lorem.txt', os.O_RDWR)

# Memory-map the file, size 0 means whole file.
# m = mmap.mmap(fd, 0)

# Read content via standard file methods.
# print(m.readline())  # prints "Hello Python!\n"

# Update content using file methods.
# m.seek(0)  # rewind
# m.write("Hello world!\n")

# Read back the changes.
# m.seek(0)
# print(m.readline())

# Close the map and the file.
# m.close()
# os.close(fd)

# Test mmap.mmap() with offset and size

# Open a file for writing.
# fd = os.open('lorem.txt', os.O_RDWR)

# Memory-map the file, size 0 means whole file.
# m = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SH
