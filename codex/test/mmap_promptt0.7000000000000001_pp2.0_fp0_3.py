import mmap
# Test mmap.mmap
filename = "test.txt"
try:
    f = open(filename, "a+")
    f.write("0123456789abcdef")
    f.close()

    f = open(filename, "rb+")
    m = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE | mmap.ACCESS_COPY)
    m.move(4, 0, 2)
    m.close()
    f.close()
    print(open(filename, "r").read())
except Exception as e:
    print(e)

# Test mmap.ALLOCATIONGRANULARITY
print(mmap.ALLOCATIONGRANULARITY)

# Test mmap.PAGESIZE
print(mmap.PAGESIZE)
