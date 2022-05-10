import mmap
# Test mmap.mmap(fileno, length[, tagname[, access[, offset]]])
# TAG(access)
m = mmap.mmap(0, 1, "mmaptest", mmap.ACCESS_WRITE)
m.write("x")
m.close()

m = mmap.mmap(0, 1, "mmaptest", mmap.ACCESS_READ)
assert m.read(1) == "x"
m.close()

m = mmap.mmap(0, 1, "mmaptest", mmap.ACCESS_COPY)
assert m.read(1) == "x"
m.write("y")
assert m.read(1) == "y"
m.close()

m = mmap.mmap(0, 1, "mmaptest", mmap.ACCESS_READ)
assert m.read(1) == "x"
m.close()

m = mmap.mmap(0, 1, "mmaptest", mmap.ACCESS_WRITE)
m.write("y")
m.close()
