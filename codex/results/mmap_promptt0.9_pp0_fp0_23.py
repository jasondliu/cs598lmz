import mmap
# Test mmap.mmap().st_size is the size of the file.
with open("test.py") as f:
    mmap_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    assert f.fileno().st_size == mmap_file.st_size
    mmap_file.close()

# Test mmap.mmap(-1).st_size is the size of the file.
with open("test.py") as f:
    mmap_file = mmap.mmap(-1, f.fileno().st_size, access=mmap.ACCESS_READ)
    assert f.fileno().st_size == mmap_file.st_size
    mmap_file.close()
