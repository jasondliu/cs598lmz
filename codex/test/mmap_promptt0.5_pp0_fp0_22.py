import mmap
# Test mmap.mmap()

# open a file
fd = os.open('test.txt', os.O_RDWR)

# create a memory map
m = mmap.mmap(fd, 0)
print(m)
# write to the file
m.write(b'abcdefghijklmnop')
print(m)
# close the file
os.close(fd)

# open the file again
fd = os.open('test.txt', os.O_RDWR)

# create a memory map
m = mmap.mmap(fd, 0)
print(m)
# read from the file
print(m.read(1))
print(m.readline())
print(m.readline())

# close the file
os.close(fd)

# open the file again
fd = os.open('test.txt', os.O_RDWR)

# create a memory map
m = mmap.mmap(fd, 0)
print(m)
# read from the file
print(m.read(1))
