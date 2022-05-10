import mmap
# Test mmap.mmap
with open('test_mmap_file.txt', 'w') as f:
    f.write('I love Python!')

with open('test_mmap_file.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print(m.read(14))

with open('test_mmap_file.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as m:
        m.write(b'0123456789abcdef')
        m.seek(0)
        print(m.read(14))

with open('test_mmap_file.txt', 'rb+') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) as m:
        m.write(b'0123456789abcdef')
        m.seek(0)
        print(m.read(14))

