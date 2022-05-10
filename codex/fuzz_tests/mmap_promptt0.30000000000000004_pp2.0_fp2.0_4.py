import mmap
# Test mmap.mmap(0, 1)
with open("foo", "wb") as f:
    f.write(b"x")
with open("foo", "rb") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()

# Test mmap.mmap(0, 1, "r")
with open("foo", "wb") as f:
    f.write(b"x")
with open("foo", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, "r")
    m.close()

# Test mmap.mmap(0, 1, "r+")
with open("foo", "wb") as f:
    f.write(b"x")
with open("foo", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, "r+")
    m.close()

# Test mmap.mmap(0, 1, "w")
with open("foo", "wb") as f:
    f.write(b"
