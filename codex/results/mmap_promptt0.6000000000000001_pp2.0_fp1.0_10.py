import mmap
# Test mmap.mmap(-1, size[, flags])
mmap.mmap(-1, 0x1000)

# Test mmap.mmap(fileno, size[, access[, offset]])
# Create a new file and write a byte to the start
f = open('mmap_testfile', 'wb')
f.write(b'\0')
f.close()

# Open the file and mmap it
f = open('mmap_testfile', 'r+b')
m = mmap.mmap(f.fileno(), 0)

# Modify the copy and write it back
m[0] = b'\xFF'
m.close()

# Read the original file to see if it was modified
f = open('mmap_testfile', 'rb')
s = f.read(1)
f.close()

# Clean up
os.remove('mmap_testfile')

# Test mmap.mmap(fileno, length[, tagname[, access[, offset]]])
# Create a new file and write a byte to the start
f = open
