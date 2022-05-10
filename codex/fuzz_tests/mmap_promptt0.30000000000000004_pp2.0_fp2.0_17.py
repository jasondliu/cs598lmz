import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0)

# Test for read-only access
with open("mmap_test.txt", "w+") as f:
    f.write("Hello, World!")
    f.flush()
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print(m.read(13))

# Test for write-only access
with open("mmap_test.txt", "w+") as f:
    f.write("Hello, World!")
    f.flush()
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) as m:
        m.write("Goodbye, World!")
    f.seek(0)
    print(f.read())

# Test for read-write access
with open("mmap_test.txt", "w+") as f:
    f.write("Hello, World!")
    f.flush()
    with mmap.mmap
