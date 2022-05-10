import mmap
# Test mmap.mmap.write_byte()

with open("test.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(b'X')
    m.seek(0, 0)
    print(m.read(10))
    m.close()
