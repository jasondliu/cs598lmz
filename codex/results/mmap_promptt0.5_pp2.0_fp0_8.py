import mmap
# Test mmap.mmap
with open('test.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), 0)
    mm.write(b'0123456789abcdef')
    mm[4:8] = b'****'
    mm.seek(0)
    print(mm.read(16))
    mm.close()

# Test mmap.ACCESS_READ
with open('test.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    try:
        mm.write(b'0123456789abcdef')
    except ValueError:
        print("ValueError raised when writing to read-only mmap")
    mm.seek(0)
    print(mm.read(16))
    mm.close()

# Test mmap.ACCESS_COPY
with open('test.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACC
