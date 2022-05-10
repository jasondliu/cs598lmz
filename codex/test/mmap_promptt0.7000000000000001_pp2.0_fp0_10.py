import mmap
# Test mmap.mmap(fd, length, tagname=None, access=ACCESS_DEFAULT, offset=0)
# with open("/proc/self/cmdline", "r+b") as f:
#     m = mmap.mmap(f.fileno(), 0, tagname="test")
#     print(m[:])
#     m.close()
#     f.write(b"new cmdline")

# Test mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT[, offset])
# import mmap
# with open("test.txt", "r+b") as f:
#     m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
#     m[:] = b"new content!"
#     m.close()
#     print(f.read())


# Test mmap.mmap(length, flags=MAP_PRIVATE, prot=PROT_READ|PROT_WRITE, access
