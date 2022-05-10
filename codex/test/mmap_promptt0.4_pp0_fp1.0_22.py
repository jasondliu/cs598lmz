import mmap
# Test mmap.mmap

# Create a file and write a few lines to it
f = open('test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read some data
print(m[:5])  # prints "01234"

# Re-size the map
m.resize(16)

# Write some data
m[6:] = 'world'

# Close the map
m.close()

# Close the file
f.close()
