import mmap
# Test mmap.mmap for writing

# Create the file
f = open('test.txt', 'w+')

# Create the mmap
m = mmap.mmap(f.fileno(), 0)

# Write to the mmap
m.write('Hello world!')

# Close the mmap
m.close()

# Close the file
f.close()
 
# Test mmap.mmap for reading

# Open the file
f = open('test.txt', 'r')

# Create the mmap
m = mmap.mmap(f.fileno(), 0)

# Read the mmap
print m.read()

# Close the mmap
m.close()

# Close the file
f.close()

# Test mmap.mmap for reading and writing

# Open the file
f = open('test.txt', 'r+')

# Create the mmap
m = mmap.mmap(f.fileno(), 0)

# Read the mmap
print m.read()

# Move back to the beginning of the mmap
m
