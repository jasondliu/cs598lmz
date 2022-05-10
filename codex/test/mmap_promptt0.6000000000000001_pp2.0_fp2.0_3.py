import mmap
# Test mmap.mmap()

# Create file
n = 1024
with open('data.bin', 'wb') as f:
    f.write(b'\x00' * n)

# Open file
with open('data.bin', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    # Assign value to every byte of the mmap
    for i in range(n):
        m[i] = i % 256
    m.close()

# Check with open
with open('data.bin', 'rb') as f:
    print(f.read(10))
# b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t'

# Test mmap.mmap()

# Create file
n = 1024
with open('data.bin', 'wb') as f:
    f.write(b'\x00' * n)

# Open file
