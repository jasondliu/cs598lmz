import mmap
# Test mmap.mmap

# Create a file
file_name = 'test.txt'
file_size = 1024

with open(file_name, 'w') as f:
    f.write('\x00' * file_size)

# Open the file
f = open(file_name, 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read the first byte
print(m[0])

# Write a new byte
m[0] = '\x01'

# Read the modified byte
print(m[0])

# Close the file
f.close()

# Open the file
f = open(file_name, 'r+')

# Read the modified byte
print(f.read(1))

# Close the file
f.close()

# Delete the file
os.remove(file_name)

# Test mmap.mmap

# Create a file
file_name = 'test.txt'
file_size = 1024

with open(file_name, 'w
