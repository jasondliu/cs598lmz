import mmap
# Test mmap.mmap

with open("/tmp/test.txt", "w") as f:
    f.write("Hello world!")

with open("/tmp/test.txt", "r") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print m.readline()
    m.close()

with open("/tmp/test.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write("Hello world!")
    m.close()

with open("/tmp/test.txt", "w") as f:
    f.write("Hello world!")

with open("/tmp/test.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(6)
    m.write("World")
    m.close()

with open("/tmp/test.txt", "r+") as f:
    m = mmap.mmap(f
