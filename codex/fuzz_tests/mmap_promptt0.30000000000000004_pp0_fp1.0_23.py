import mmap
# Test mmap.mmap

# Create a file
f = open('test.txt', 'w+')
f.write('Hello World')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory map
m = mmap.mmap(f.fileno(), 0)

# Read from the memory map
print(m.readline())

# Close the memory map
m.close()

# Close the file
f.close()

# Delete the file
os.remove('test.txt')

# Test mmap.ACCESS_READ

# Create a file
f = open('test.txt', 'w+')
f.write('Hello World')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory map
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read from the memory map
print(m.readline())

# Close the memory map
m.close()

# Close
