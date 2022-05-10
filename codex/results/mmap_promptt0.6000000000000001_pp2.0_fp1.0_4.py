import mmap
# Test mmap.mmap()

# Create a file and write a few lines to it
f = open('test.txt', 'w+')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')
f.write('Hello, world!\n')

# Set the position to the beginning of the file
f.seek(0)

# Create a
