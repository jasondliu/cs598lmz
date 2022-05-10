import bz2
# Test BZ2Decompressor

# Create a compressed file
data = b'The same line, over and over.\n'
data = data * 1024

with open('string.bz2', 'wb') as f:
    f = bz2.BZ2File(f, 'w')
    f.write(data)
    f.close()

# Decompress it
with open('string.bz2', 'rb') as f:
    f = bz2.BZ2File(f)
    data2 = f.read()
    f.close()

# Check if it is the same
assert data == data2

# Clean up
