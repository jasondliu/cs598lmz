import mmap
# Test mmap.mmap
with open('test.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), 0)
    mm.write(b'0123456789abcdef')
    mm[5] = b'5'
    print(mm[5])
    print(mm[1:10])
    print(mm.readline())
    mm.seek(0)
    print(mm.readline())
    mm.close()
# Test mmap.ACCESS_READ
with open('test.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(mm[0])
    mm[0] = b'0'
    mm.close()
# Test mmap.ACCESS_COPY
with open('test.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
