import mmap
# Test mmap.mmap()
def test_mmap():
    fd = os.open(tmp_file, os.O_RDWR)
    mem = mmap.mmap(fd, 100)
    mem.write(b"Hello, world")
    mem.seek(0)
    print(mem.read(len("Hello, world")))
    mem.close()
    os.close(fd)
    os.remove(tmp_file)

# Test mmap.mmap() with default value of access
def test_mmap_access():
    fd = os.open(tmp_file, os.O_RDWR)
    mem = mmap.mmap(fd, 100)
    mem.write(b"Hello, world")
    mem.seek(0)
    print(mem.read(len("Hello, world")))
    mem.close()
    os.close(fd)
    os.remove(tmp_file)

# Test mmap.mmap() with access = mmap.ACCESS_COPY
def test_mmap_access_copy():
    fd
