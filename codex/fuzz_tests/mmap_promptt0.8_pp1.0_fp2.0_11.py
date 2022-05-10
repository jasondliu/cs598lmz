import mmap
# Test mmap.mmap
with open('mmaptest.txt', 'w+b') as f:
    mem = mmap.mmap(f.fileno(), 0)  # mem is the mmap object
    mem[0:4] = b'MMAP'
    mem.close()
with open('mmaptest.txt', 'rb') as f:
    data = f.read()
print(data)

# Test with os.open
fd = os.open('mmaptest.txt', os.O_RDWR)
mem = mmap.mmap(fd, 0, prot=mmap.PROT_READ | mmap.PROT_WRITE)
mem[0:4] = b'MMAP'
mem.close()
os.close(fd)
with open('mmaptest.txt', 'rb') as f:
    print(f.read())

# Test mmap.mmap.tell
with open('mmaptest.txt', 'w+b') as f:
    mem = mmap.mmap(f.fileno(), 0)
    mem.seek(1000)
