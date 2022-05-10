import mmap

with open("test.txt", "w+") as f:
    f.write("This is a test file.\n")
    f.write("Now we are going to use mmap.\n")

with open("test.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write("Hello, world, amazing!")
    m.close()

with open("test.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read())
    m.close()
