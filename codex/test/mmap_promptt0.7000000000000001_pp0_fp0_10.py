import mmap
# Test mmap.mmap
x = mmap.mmap(-1, mmap.PAGESIZE)
s = x.read()
print(len(s), repr(s))

# Test mmap.mmap2
x = mmap.mmap(-1, mmap.PAGESIZE * 2,
              offset=mmap.PAGESIZE)
try:
    s = x.read()
    print(len(s), repr(s))
except OSError as e:
    print("OSError", e)

# Test mmap.mmap from a file descriptor
with open("/dev/zero", "r+b") as f:
    x = mmap.mmap(f.fileno(), mmap.PAGESIZE, access=mmap.ACCESS_WRITE)
    s = x.read()
    print(len(s), repr(s))
    x.write(b"X")
    x.seek(0)
    print(x.read(1))
    print(x.read(1))
    x.close()

