import mmap
# Test mmap.mmap.read() and mmap.mmap.write()

with open('test.txt', 'wb') as f:
    f.write(b'0123456789abcdef')

with open('test.txt', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.read(5)
    m.write(b'ABCDE')
    m.seek(0)
    print(m.read(16))
    m.close()

with open('test.txt', 'rb') as f:
    print(f.read())

# Test mmap.mmap.read_byte() and mmap.mmap.write_byte()

with open('test.txt', 'wb') as f:
    f.write(b'0123456789abcdef')

with open('test.txt', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.read_byte()
    m.write_byte(b'A')
   
