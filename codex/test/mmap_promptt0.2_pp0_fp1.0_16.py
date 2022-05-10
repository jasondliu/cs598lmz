import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Print content
print(m.readline())

# Update content
m.seek(0)
m.write(b'0123456789abcdef')

# Flush changes
m.flush()

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Print content
print(m.readline())

# Update content
m.seek(0)
m.write(b'0123456789abcdef')

# Flush changes
m.flush()

# Close the map
m.close()

# Close the file
f.close()


