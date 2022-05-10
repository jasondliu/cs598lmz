import mmap
# Test mmap.mmap

# Create a new file and memory-map it
f = open('hello.txt', 'w+')
f.write('hello world!')
f.close()

f = open('hello.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Read from the mmap
