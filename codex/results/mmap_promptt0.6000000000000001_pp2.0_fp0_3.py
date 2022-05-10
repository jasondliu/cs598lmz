import mmap
# Test mmap.mmap()

print("\nmmap.mmap()")

# Create a memory map to some file.  The file must exist, so it
# must be created first.
f = open("data.dat", "wb")

# Zero out the file so there's something to look at.
# (Probably not needed)
f.seek(10*1024*1024 - 1)
f.write(b'\x00')
f.close()

# Open the file for reading and writing so it can be mmap'ed
f = open("data.dat", "r+b")

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Print the first 10 bytes of the file
print('First 10 bytes via read :', m.read(10))

# Print the first 10 bytes via slice
print('First 10 bytes via slice: ', m[:10])

# Update the first 10 bytes
m[:10] = b'Hello World'

# Read the change back ...
m.seek(0)
print('
