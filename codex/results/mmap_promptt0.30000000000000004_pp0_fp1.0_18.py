import mmap
# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')
f.write('Hello world!')
f.close()

# Open file with mmap
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Read file
print(m.readline())

# Write to file
m.seek(0)
m.write('Hello Python!')

# Close file
m.close()
f.close()

# Open file with mmap
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Read file
print(m.readline())

# Close file
m.close()
f.close()

# Delete file
os.remove('test.txt')

# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')
f.write('Hello world!')
f.close()

# Open file with mmap
f = open
