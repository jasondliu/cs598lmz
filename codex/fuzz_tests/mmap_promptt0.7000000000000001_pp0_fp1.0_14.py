import mmap
# Test mmap.mmap()
print(type(mmap.mmap(-1, 1)))

# Test mmap.mmap(fd, size)
with open(__file__, "r+b") as fp:
    m = mmap.mmap(fp.fileno(), 0)
    print(repr(m.readline()))
    print(m.tell())
    m.seek(0)
    print(repr(m.readline()))
    print(m.tell())
    m.seek(0, os.SEEK_END)
    print(m.tell())
    m.close()

# Test mmap.mmap(fd, size, access)
with open(__file__, "r+b") as fp:
    m = mmap.mmap(fp.fileno(), 0, mmap.ACCESS_READ)
    print(repr(m.readline()))
    m.close()

# Test mmap.mmap(fileno, length[, tagname[, access[, offset]]])
with open(__file__, "
