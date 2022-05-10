import mmap
# Test mmap.mmap

with open("/tmp/test.txt", "w") as f:
    f.write("Hello world!")

with open("/tmp/test.txt", "r") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
