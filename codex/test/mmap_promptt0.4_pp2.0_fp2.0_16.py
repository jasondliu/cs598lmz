import mmap
# Test mmap.mmap()

# Create a file and write some data to it
with open('/tmp/test.txt', 'w+') as f:
    f.write('Hello world!')

# Open the file in read-only mode and mmap it
with open('/tmp/test.txt', 'r') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)

# Read some data from the mmap
print(m.readline())

# Close the mmap
m.close()

# Open the file in write-only mode and mmap it
with open('/tmp/test.txt', 'w') as f:
    m = mmap.mmap(f.fileno(), 0)

# Write some data to the mmap
m.write(b'Hello world!')

# Close the mmap
m.close()

# Open the file in read-only mode and mmap it
