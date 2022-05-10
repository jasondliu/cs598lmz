import mmap
# Test mmap.mmap(0, 4096, "a", mmap.MAP_PRIVATE, -1, 0)

with open("/tmp/text", "w") as f:
    f.write("foo")

m = mmap.mmap(0, 4096, "a", mmap.MAP_PRIVATE, -1, 0)
m.write("bar")
m.seek(0)
