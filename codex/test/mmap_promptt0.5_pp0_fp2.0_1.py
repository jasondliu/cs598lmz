import mmap
# Test mmap.mmap(fileno, length)
with open(filename, "wb") as f:
    f.write(b"\x00" * 100)

m = mmap.mmap(f.fileno(), 100)
m[0] = b"\x01"
m.close()

with open(filename, "rb") as f:
    print(f.read(1))
    print(f.read(99))

# Test mmap.mmap(fileno, length, access=ACCESS_WRITE)
with open(filename, "wb") as f:
    f.write(b"\x00" * 100)

m = mmap.mmap(f.fileno(), 100, mmap.ACCESS_WRITE)
m[0] = b"\x01"
m.close()

with open(filename, "rb") as f:
    print(f.read(1))
    print(f.read(99))

# Test mmap.mmap(fileno, length, access=ACCESS_READ)
