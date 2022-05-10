import mmap
# Test mmap.mmap
#
# https://docs.python.org/3/library/mmap.html

# Create a new file in read/write mode
f = open("hello.txt", "w+")
# Create a memory-map to an integer
#   - size is number of bytes
#   - access=mmap.ACCESS_WRITE means read and write access
m = mmap.mmap(f.fileno(), 0)
# Write the bytes 5 and 6 to the buffer
m[0:1] = b'5'
m[1:2] = b'6'
# Flush the changes to disk
m.flush()
# Close the memory map
m.close()
# Close the file
f.close()

# Re-open the file and map it
f = open("hello.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
# Read from the memory map
print("First two bytes via read():", m.read(2))
# Reset the file pointer to the beginning
m.seek(0)
# Read from the memory map via
