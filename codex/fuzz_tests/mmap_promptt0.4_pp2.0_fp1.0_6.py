import mmap
# Test mmap.mmap
m = mmap.mmap(-1, 13)
m.write(b"Hello, World!")
m.seek(0)
print(m[:])
m.close()

# Test mmap.mmap() with a file
with open('lorem.txt', 'r') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    m.close()

# Test mmap.mmap() with a file descriptor
with open('lorem.txt', 'r') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m[:])
    m.close()

# Test mmap.mmap() with a file descriptor and offset
with open('lorem.txt', 'r') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m[5:10])
    m.close()

# Test mmap.mm
