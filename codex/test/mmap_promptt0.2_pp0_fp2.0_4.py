import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'w+')

# Write to file
f.write('Hello World!')
f.write('This is our new text file')
f.write('and this is another line.')
f.write('Why? Because we can.')

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read contents
print(m.readline())

# Update content
m.seek(0)
m.write(b'Hello Python!')

# Close map
m.close()

# Close file
f.close()

# Open file
f = open('test.txt', 'r')

# Read contents
print(f.read())

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)
