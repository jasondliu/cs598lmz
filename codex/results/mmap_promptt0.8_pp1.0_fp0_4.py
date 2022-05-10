import mmap
# Test mmap.mmap.
f = open('test.mmap', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Fill the contents with ASCII upper case.
m.resize(128*1024*1024)
m.write('ABCDEFGHIJKLMNOP' * (128*1024*1024/16))

# Read from the mmap and print some contents.
print m.read(1024)
print m.read(1024)

# Change some bytes.
m.seek(1024)
m.write('a' * 1024)
m.seek(0)

# Print the modified contents.
print m.read(1024)

# Close the mmap.
m.close()

# Test mmap.mmap() with offset and size.
f = open('test.mmap', 'r+')
m = mmap.mmap(f.fileno(), 1024*1024, access=mmap.ACCESS_WRITE, offset=1024*1024)

# Fill the contents with ASCII lower case.
m.write('abcdefghijklmnop'
