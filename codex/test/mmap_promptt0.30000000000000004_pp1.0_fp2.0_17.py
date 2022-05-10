import mmap
# Test mmap.mmap()
with open('test.txt', 'w') as f:
    f.write('0123456789abcdef')
with open('test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    print(m[1])
    m.seek(5)
    print(m.read(1))
    m.write(b'1')
    m.seek(0)
    print(m.read(16))
    m.close()

# Test mmap.mmap(fileno, length)
with open('test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 16)
    print(m[:])
    m.close()

# Test mmap.mmap(fileno, length, tagname)
with open('test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 16, tagname='test')
