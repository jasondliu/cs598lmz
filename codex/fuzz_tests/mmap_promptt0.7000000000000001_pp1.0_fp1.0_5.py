import mmap
# Test mmap.mmap and mmap.mmap().read()

# Test the various ways to create an mmap object.

import mmap

# Size of mapping (must be <= file size)
mapping_size = 10000

# Create a file and fill it with null bytes
with open('test.txt', 'w+b') as f:
    f.seek(mapping_size)
    f.write(b'\0')
    f.flush()

# Use the open file
with open('test.txt', 'r+b') as f:
    # Create an mmap backed by the file
    m = mmap.mmap(f.fileno(), mapping_size)
    # Write some data using write_byte
    m[0] = b'a'
    m.write_byte(b'b')
    # Read back the data using readline
    print(m.readline())
    # Write more data using write
    m.seek(0)
    m.write(b'0123456789abcdef')
    # Read back the data using read
    m.seek
