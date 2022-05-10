import mmap
# Test mmap.mmap

import mmap

with open("test.txt", "w+") as f:
    f.write("Hello World!" * 1024 * 1024 * 16)

with open("test.txt") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write("foo")
    print(m.readline())
    m.close()

print("EOL")
