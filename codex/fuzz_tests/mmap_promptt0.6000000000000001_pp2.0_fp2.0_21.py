import mmap
# Test mmap.mmap
f = open('data.bin', 'wb')
f.write(b'Hello Python!')
f.close()
f = open('data.bin', 'r+b')
m = mmap.mmap(f.fileno(), 0)
m.seek(0)
print(m.readline())
m.seek(0)
m.write(b'Hello World!')
m.seek(0)
print(m.readline())
m.close()
f.close()

# Test mmap.mmap(0)
with open('data.bin', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'Hello Python!')
    m.seek(0)
    print(m.readline())

# Test mmap.mmap(0, access=mmap.ACCESS_WRITE)
with open('data.bin', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WR
