import mmap
# Test mmap.mmap instance creation
file = open("test.txt", "r+")
# Create an anonymous memory map
m = mmap.mmap(file.fileno(), 0)
# Write the text to the memory map
m[0:] = "Hello Python world"
m.flush()  # Push data to file
print m[:]  # Print text
m.close()
file.close()
# Test mmap.mmap size and offset arguments
# print 'mmap:', mmap.mmap.__doc__
# print 'mmap.mmap:', mmap.mmap.mmap.__doc__
file = open("test.txt", "r+")
# Create a memorymap without offset and size
# To run the example without file truncation comment the following line
m = mmap.mmap(file.fileno(), 0)
m.seek(0, 2)  # move to the end of the file
size = m.tell()
# move to the beginning of the file
m.seek(0, 0)
# Get the string from memory map
mem_string = m.read(size)
