import mmap
# Test mmap.mmap
with open("python.txt", "r+b") as file:
    data = mmap.mmap(file.fileno(), 0)
    print("Before:", data.readline())
    data.seek(0)
    data.write(b"0123456789abcdef")
    data.seek(0)
    print("After:", data.readline())
    data.close()

# Test mmap.mmap
size = os.stat("python.txt").st_size
with open("python.txt", "r+b") as file:
    data = mmap.mmap(file.fileno(), size)
    print("Before:", data[:])
    data.seek(0)
    data.write(b"0123456789abcdef")
    data.seek(0)
    print("After:", data.read(size))
    data.close()
