import mmap
# Test mmap.mmap
f = open("tmp.txt", "rb")
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(m.readline())
m.close()
f.close()
# Test mmap.mmap with "with" statement
with open("tmp.txt", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.readline())
    m.close()
# Test mmap.mmap with "with" statement
with open("tmp.txt", "rb") as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print(m.readline())
