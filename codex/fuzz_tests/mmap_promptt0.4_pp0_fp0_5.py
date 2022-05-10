import mmap
# Test mmap.mmap

# Create a new file and memory-map it
f = open('hello.txt', 'w+')
f.write('hello world!')
f.close()

f = open('hello.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Read from the mmap
print m[:]

# Update the mmap
m[6:] = 'world'

# Flush changes to disk
m.flush()

# Close the mmap
m.close()

# Reopen the file and read the changes
f = open('hello.txt', 'r+')
print f.readline()
f.close()

os.remove('hello.txt')

# Test mmap.mmap with offset and size

# Create a new file and memory-map it
f = open('hello.txt', 'w+')
f.write('hello world!')
f.close()

f = open('hello.txt', 'r+')
m = mmap.mmap(f.fileno(), 12, offset=6)
