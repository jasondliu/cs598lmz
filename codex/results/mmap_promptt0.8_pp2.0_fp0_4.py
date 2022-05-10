import mmap
# Test mmap.mmap() for creating an object that maps
# a file's contents into memory.

with open("./test.log", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    data = m.read()
    print(data)
    print(type(data))


# with open("./test2.log", "wb") as f:
#     f.write(data)

# with open("./test.log", "rb") as f:
#     m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
#     for i in range(0, m.size(), 7):
#         print('[{0}] {1}'.format(i, m.read(7)))
