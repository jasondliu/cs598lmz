import mmap
# Test mmap.mmap()

# Open a file
fd = os.open('/tmp/test.txt', os.O_CREAT | os.O_RDWR)

# Write a few lines
os.write(fd, b'Hello world!\n')
os.write(fd, b'Bye bye world!\n')

# Close the file
os.close(fd)

# Open the file
fd = os.open('/tmp/test.txt', os.O_RDWR)

# Create a memory map
m = mmap.mmap(fd, 0)

# Read the file
print(m.readline())
print(m.readline())

# Close the file
m.close()
os.close(fd)

# Open the file
fd = os.open('/tmp/test.txt', os.O_RDWR)

# Create a memory map
m = mmap.mmap(fd, 0)

# Read the file
print(m.readline())
print(m.readline())

# Close the file
m.close()
