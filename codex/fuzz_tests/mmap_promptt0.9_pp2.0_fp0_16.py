import mmap
# Test mmap.mmap() after creating and writing to a file,
# using both fd and pathname arguments.

import mmap


def write_testfile(filename):
    with open(filename, "w+") as f:
        f.write("hello world\n")
        f.write("goodbye world\n")
        f.flush()


f = open("testfile", "w+")
f.write("hello world\n")
f.write("goodbye world\n")
f.flush()

# fd-based mmap
m1 = mmap.mmap(f.fileno(), 0)
assert m1.readline() == b"hello world\n"
assert m1.readline() == b"goodbye world\n"

# pathname-based mmap
m2 = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
assert m2.readline() == b"hello world\n"
assert m2.readline() == b"goodbye world\n"


# fd-based mmap

