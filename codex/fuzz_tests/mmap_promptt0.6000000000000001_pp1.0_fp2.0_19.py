import mmap
# Test mmap.mmap and mmap.mmap.read
with open('lorem.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print('First 10 bytes via read :', m.read(10))
        print('First 10 bytes via slice:', m[:10])
        print('2nd   10 bytes via read :', m.read(10))

# Test mmap.mmap.find
with open('lorem.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print('Lorem Ipsum via find :', m.find(b'Lorem'))

# Test mmap.mmap.rfind
with open('lorem.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print('Lorem Ipsum via rfind :', m.rfind(
