import mmap
# Test mmap.mmap()
with open('data.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), 0)
    mm.write(b'0123456789abcdef')
    mm.seek(0)
    print(mm.read(10))
    print(mm.read(5))
    mm.seek(0)
    print(mm.read(10))
    mm.close()

# Test mmap.mmap(fileno, length)
with open('data.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), 15)
    mm.write(b'0123456789abcdef')
    mm.seek(0)
    print(mm.read(10))
    print(mm.read(5))
    mm.seek(0)
    print(mm.read(10))
    mm.close()

# Test mmap.mmap(fileno, length, access=ACCESS_READ)
with open('data.txt', 'r+') as f:
   
