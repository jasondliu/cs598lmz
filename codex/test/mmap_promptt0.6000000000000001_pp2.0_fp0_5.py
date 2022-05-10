import mmap
# Test mmap.mmap

with open("test.txt", "wb") as f:
    f.write("hello world")

with open("test.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    print("before:" + m.readline().rstrip())
