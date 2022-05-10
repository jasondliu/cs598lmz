import mmap
# Test mmap.mmap()

# Create file
f = open('test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

# Memory-map the file, size 0 means whole file
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Read contents
print 'First 10 bytes via read :', m.read(10)

# Seek 10 bytes from current position
m.seek(10)

# Write 'abcdefghij'
m.write('abcdefghij')

# Flush changes
m.flush()

# Read from position 0 again
m.seek(0)
print 'First 10 bytes via read :', m.read(10)

# Close the map
m.close()

# Close the file
f.close()
