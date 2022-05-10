import mmap
# Test mmap.mmap.read_byte(offset)
with open("test.txt", "w+") as f:
    f.write("hello world")
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0)
    print(m.read_byte(0))

# Test mmap.mmap.read_line()
with open("test.txt", "w+") as f:
    f.write("hello world\n")
    f.write("hello world")
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())

# Test mmap.mmap.read()
with open("test.txt", "w+") as f:
    f.write("hello world")
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(6))

