import mmap
# Test mmap.mmap(id, length, access=mmap.ACCESS_WRITE) 

# Open file to mmap
f = open("test", "r+b") 
# f = open("test", "w+b") 

# Get mmap object
m = mmap.mmap(f.fileno(), 0) 
# m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) 

# Get string from mmap object
s = m.read(10) 
print(s)
print(type(s))

# Close file
f.close() 

# Close mmap object
