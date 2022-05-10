import mmap
# Test mmap.mmap.read_byte()

# Create a file and write a byte
with open('test.txt', 'wb') as f:
    f.write(b'a')

# Open the file using mmap
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read the byte
print(m.read_byte())

# Close the file
m.close()

# Delete the file
os.remove('test.txt')

# This should print 97

# Create a file and write a byte
with open('test.txt', 'wb') as f:
    f.write(b'a')

# Open the file using mmap
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read the byte
print(m.read_byte())

# Close the file
m.close()

# Delete the file
os.remove('test.txt')

