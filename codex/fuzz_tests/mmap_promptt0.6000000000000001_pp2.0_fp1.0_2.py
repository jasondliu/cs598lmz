import mmap
# Test mmap.mmap.flush()

# Create a file to be used as backing store
with open('tmp', 'w+b') as f:
    f.write(b'\0' * 100)

# Map the file
m = mmap.mmap(f.fileno(), 0)

# Modify the mapped region
m[0:5] = b'Hello'

# Flush the changes
m.flush()

# Unmap the region
m.close()
