import mmap
# Test mmap.mmap

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read some data
print(m.readline())

# Re-seek to beginning
m.seek(0)

# Overwrite data
m.write('0123456789abcdef')

# Close the map
m.close()

# Close the file
f.close()

# Open file
f = open('test.txt', 'r+')

# Read the entire file
print(f.read())

# Close the file
f.close()

# Delete the file
os.remove('test.txt')

# Test mmap.mmap

# Open file
f = open('test.txt', 'w+')

# Write some data
f.write('0123456789abcdef')

# Close the file
f.close()

# Open file
