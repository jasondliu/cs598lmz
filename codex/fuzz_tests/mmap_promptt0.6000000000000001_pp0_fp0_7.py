import mmap
# Test mmap.mmap()

m = mmap.mmap(-1, 1)
print(m)
m.write(b"a")
m.seek(0)
print(m.read())

m.close()
# Test mmap.mmap() with a file

with open("mmap_test.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("mmap_test.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    m.seek(0)
    m.write(b"Hello world!\n")
    m.seek(0)
    print(m[:])
    m.close()

os.remove("mmap_test.txt")
# Test mmap.mmap() with a file, using access=mmap.ACCESS_WRITE

with open("mmap_test.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open
