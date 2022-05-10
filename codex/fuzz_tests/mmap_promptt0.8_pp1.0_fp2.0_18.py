import mmap
# Test mmap.mmap to read file

# Using mmap.mmap(handle, size)
# The handle is the file opened by using open
# The size is the number we want to read
# If size is 0, the size will be the same of the file opened.
# The return value is the same as read()
import os

file = open("demofile.txt", "r+")

# Get the size of the file
st_results = os.stat("demofile.txt")
st_size = st_results[6]

print("The size of the file is: ", st_size)

mm = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

print(mm.readline())

print(mm[:4])

mm.close()

# Test mmap.mmap to write file

# Using mmap.mmap(file.fileno(), size)
# The file is the file opened by using open
# The size is the number we want to find
# If size is 0, the size will be the same of the
