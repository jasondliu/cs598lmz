import mmap
# Test mmap.mmap object

# Open file
f = open('data.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.seek(0)

# Create memory map
m = mmap.mmap(f.fileno(), 16)

# Read from memory map
print(m.read(16))

# Close file
f.close()

# Close memory map
m.close()

# Test mmap.mmap object

# Open file
f = open('data.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.seek(0)

# Create memory map
m = mmap.mmap(f.fileno(), 16)

# Read from memory map
print(m.read(16))

# Close file
f.close()

# Close memory map
m.close()

# Test mmap.mmap object

# Open file
f = open('data.txt', 'w+')

# Write to file
f.write
