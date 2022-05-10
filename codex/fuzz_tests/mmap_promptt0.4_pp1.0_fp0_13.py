import mmap
# Test mmap.mmap()
# Create a file and write a few things to it
with open("hello.txt", "w+") as f:
    f.write("Hello Python! Love, User")
# Open the file
f = open("hello.txt", "r+")
# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# Read from the memory-map
print(m.readline())
# Close the map
m.close()
# Close the file
f.close()

# Test mmap.mmap()
# Create a file and write a few things to it
with open("hello.txt", "w+") as f:
    f.write("Hello Python! Love, User")
# Open the file
f = open("hello.txt", "r+")
# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# Read from the memory-map
print(m.readline())
# Close the map
m.close()
#
