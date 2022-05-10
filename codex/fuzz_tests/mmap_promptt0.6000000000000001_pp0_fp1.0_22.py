import mmap
# Test mmap.mmap()

print(os.getcwd())

# Open file for reading and writing
f = open('lorem.txt', 'r+b')

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# Read contents
print(m[:10])
# Update content using slice assignment
# ... and read again using `mmap`
m[6:11] = b' world'
m.seek(0)  # rewind
print(m.readline())
# Close the map
m.close()
# Close the file
f.close()
