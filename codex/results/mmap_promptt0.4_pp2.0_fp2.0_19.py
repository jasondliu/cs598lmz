import mmap
# Test mmap.mmap()

# Create a file
f = open('test.txt', 'w+')

# Write to the file
f.write('Hello World')

# Close the file
f.close()

# Open the file again
f = open('test.txt', 'r+')

# Map the file
mm = mmap.mmap(f.fileno(), 0)

# Read the file
print(mm.readline())

# Close the file
f.close()

# Open the file again
f = open('test.txt', 'r+')

# Map the file
mm = mmap.mmap(f.fileno(), 0)

# Read the file
print(mm.readline())

# Close the file
f.close()

# Open the file again
f = open('test.txt', 'r+')

# Map the file
mm = mmap.mmap(f.fileno(), 0)

# Read the file
print(mm.readline())

# Close the file
f.close()

# Open the file again

