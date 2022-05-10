import mmap
# Test mmap.mmap(), mmap.close()

with open("foo.txt", "w+") as f:
    f.write("hello")
    f.flush()
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.close()
