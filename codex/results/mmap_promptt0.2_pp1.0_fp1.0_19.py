import mmap
# Test mmap.mmap()
with open("test.txt", "w+") as f:
    f.write("Hello world!")
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())
    m.seek(0)
    m.write_byte(b'J')
    m.seek(0)
    print(m.readline())
    m.close()

# Test mmap.mmap() with offset
with open("test.txt", "w+") as f:
    f.write("Hello world!")
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0, offset=6)
    print(m.readline())
    m.seek(0)
    m.write_byte(b'J')
    m.seek(0)
    print(m.readline())
    m.close()

# Test mmap.mmap() with size
with open("test.txt", "w+") as f:
    f.write("Hello
