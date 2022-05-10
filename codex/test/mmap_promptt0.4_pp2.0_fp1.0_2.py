import mmap
# Test mmap.mmap() function
# https://www.tutorialspoint.com/python/python_memory_mapping.htm
# https://stackoverflow.com/questions/1425493/replace-string-in-text-file-with-python

# Open a file
fd = os.open( "test.txt", os.O_RDWR )

# Create a memory-map to the file.
m = mmap.mmap(fd, 0)

# Print the content of the file
print(m.readline())

# Close the opened file
os.close(fd)

# Open a file
fd = os.open( "test.txt", os.O_RDWR )

# Create a memory-map to the file.
m = mmap.mmap(fd, 0)

# Replace the first line
m.seek(0) # rewind
m.write('This is the first line.\n')

# Print the content of the file
m.seek(0) # rewind
print(m.readline())

# Close the opened file
os.close
