import mmap
# Test mmap.mmap
f = open('test.bin', 'w+b')
f.write(b'0123456789abcdef' * 1024 * 1024)
m = mmap.mmap(f.fileno(), 0)
# Read from mmap
print(m[0])
print(m[0:3])
print(m[10:15])
# Modify mmap
m[0] = b'!'
m[2:5] = b'23'
# Flush changes
m.flush()
# Close file
m.close()
f.close()

# Test mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0)
# f = open('test.bin', 'w+b')
# f.write(b'0123456789abcdef' * 1024 * 1024)
# m = mmap.mmap(f.fileno(), 1024**2, access=mmap.ACCESS_WRITE)

