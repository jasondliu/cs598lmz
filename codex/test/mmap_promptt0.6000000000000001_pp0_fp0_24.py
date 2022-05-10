import mmap
# Test mmap.mmap()

# Open as read/write to create file
# write copy of file to disk
f = open("testmmap.txt", "w+")
f.write("This is a test string")
f.close()

# Open file for reading
f = open("testmmap.txt", "r")
# Map file to memory
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
# Print contents using standard file methods
print(m.readline())
# Close the map
m.close()

# Open file for reading
f = open("testmmap.txt", "r")
# Map file to memory
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
# Print contents using standard file methods
print(m.readline())
# Close the map
m.close()

# Open file for reading
f = open("testmmap.txt", "r")
# Map file to memory
