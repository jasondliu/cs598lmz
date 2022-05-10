import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.write('ABCDEF')

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print content
print(m.readline())

# Close file
f.close()


# Test mmap.mmap()

# Open file
f = open('test.txt', 'w+')

# Write to file
f.write('0123456789abcdef')
f.write('ABCDEF')

# Close file
f.close()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print content
print(m.readline())

# Close file
f.close()
