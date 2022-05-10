import mmap
# Test mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE, access=ACCESS_DEFAULT)

# f = open('test.txt', 'r+')
# m = mmap.mmap(f.fileno(), 0)
# m.write(b'0123456789abcdef')
# m.seek(0)
# print(m.read(10))
# m.seek(3)
# m.write(b'XXXX')
# m.seek(0)
# print(m.read(10))
# m.close()
# f.close()

# Test mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE, access=ACCESS_DEFAULT)

# f = open('test.txt', 'w+')
# m = mmap.mmap(f.fileno(), 0)
# m.write(b'0123456789abcdef')
# m.seek(0)
# print(m.read(10))
# m.seek(
