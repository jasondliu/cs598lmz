import mmap
# Test mmap.mmap.write() method
#
# Create a new file, write to it, and read from it
# using mmap.

# Open file for reading and writing.
# Create it if it doesn't exist.
# Truncate it to zero length if it does exist.
# fd = os.open('test.txt', os.O_RDWR | os.O_CREAT | os.O_TRUNC)
#
# os.write(fd, b'This is a test\n')
# os.close(fd)
#
# fd = os.open('test.txt', os.O_RDWR)
# m = mmap.mmap(fd, 0)
#
# print(m.readline())
# print(m.readline())
#
# m.seek(0)
# m.write(b'R')
# m.seek(11)
# m.write(b'test')
# m.seek(0)
# print(m.readline())
#
# m.close()
# os.close(fd)

# with open
