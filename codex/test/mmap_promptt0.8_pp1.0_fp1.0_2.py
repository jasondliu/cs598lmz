import mmap
# Test mmap.mmap()
# Requires a file named test.data, which is a binary file.
f = open("test.data","r+")
# Access contents of test.data binary file.
m = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_COPY)
# The following will access the location 34, in the file.
m[34]

# The following will access the location from 10 to 19.
# The 10 represents the starting point, and the 19 represents the end point.
m[10:19]

# The following will set the value of the value at location 15 to 1.
m[15] = 1

# The following will set the value of the value at location 5 to 1.
m[5:6] = '\x00'

# The following will set the value of the value at location 6 to 1.
m[6:7] = '\xff'

# The following will set the value of the value at location 7 to  1.
m[7:8] = '\x00'

# The following will set the value of the value
