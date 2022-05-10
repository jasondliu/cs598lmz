import mmap
# Test mmap.mmap()

import mmap

def write_mmap(m):
    m[1:3] = b"\x00\xff"

def write_file(f):
    f.seek(1)
    f.write(b"\x00\xff")

with open("foo.txt", "w+") as f:
    f.write("Hello world!")
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    write_mmap(m)
    write_file(f)
    print(m.read())
