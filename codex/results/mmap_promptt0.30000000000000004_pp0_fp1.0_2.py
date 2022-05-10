import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'w+b')

# Write to file
f.write(b"Hello Python!\n")

# Close file
f.close()

# Open file
f = open('test.txt', 'r+b')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read from memory map
print(m.readline())

# Update memory map with new data
m.seek(0)
m.write(b'Hello World!\n')

# Close file
f.close()

# Open file
f = open('test.txt', 'r')

# Read from file
print(f.readline())

# Close file
f.close()

# Open file
f = open('test.txt', 'w+b')

# Write to file
f.write(b"Hello Python!\n")

# Close file
f.close()

# Open file
f = open('test.txt', 'r+b')

#
