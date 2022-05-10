import mmap
# Test mmap.mmap()
with open('/Users/shenghua/workspace/python/mmap/test.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), 0)
    # print(mm.readline())
    print(mm.read(5))
    mm.seek(0)
    print(mm.readline())
    mm.seek(0)
    print(mm.readline())
    mm.write(b'0123456789abcdef')
    mm.seek(0)
    print(mm.read(16))
    mm.close()


# from mmap import mmap, ACCESS_READ
# fd = os.open('/Users/shenghua/workspace/python/mmap/test.txt', os.O_RDONLY)
# m = mmap(fd, 0, access=ACCESS_READ)
# print(m[:5])
# print(m.rfind(b'\n'))
# print(m.rfind(b'\n', 0, 50))

