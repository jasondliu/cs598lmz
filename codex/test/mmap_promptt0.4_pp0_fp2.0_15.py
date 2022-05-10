import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# https://docs.python.org/3/library/mmap.html

# Create a new file and memory-map it
f = open('hello.txt', 'w+')
f.write('hello world!')
f.close()

f = open('hello.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using slice notation;
# note that new content must have same size
m[6:] = b'world'
m.close()

# Verify that changes were made
with open('hello.txt', 'r') as f:
    print(f.readline())

# Clean up
os.remove('hello.txt')

# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
