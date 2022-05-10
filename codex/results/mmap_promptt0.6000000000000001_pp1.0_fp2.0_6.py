import mmap
# Test mmap.mmap
# https://docs.python.org/3/library/mmap.html

# Create file
f = open('hello.txt', 'w+')

# Add content
f.write('hello world')
f.close()

# Open with mmap
f = open('hello.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Print content
print(m.readline())

# Update content
m.seek(0)
m.write(b'hello beautiful world')
m.close()

# Print file
f = open('hello.txt', 'r')
print(f.read())

# Close file
f.close()

# Remove file
os.remove('hello.txt')

# Test mmap.mmap
# https://docs.python.org/3/library/mmap.html

# Create file
f = open('hello.txt', 'w+')

# Add content
f.write('hello world')
f.close()

# Open with mmap
f = open('hello
