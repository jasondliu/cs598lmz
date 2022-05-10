import mmap
# Test mmap.mmap()

# Create a file object
f = open('data.bin', 'w+b')

# Fill it with some data
f.write(b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a')

# Create a memory-mapped file
m = mmap.mmap(f.fileno(), 0)

# Read the first byte
print(m[0])

# Read the first four bytes
print(m[:4])

# Read the last four bytes
print(m[-4:])

# Read the next four bytes
print(m.read(4))

# Read the next four bytes
print(m.read(4))

# Reset the read position
m.seek(0)

# Read the next four bytes
print(m.read(4))

# Move the read position
m.seek(4)

# Read the next four bytes
print(m.read(4))

# Move the read position
m.seek(6)

#
