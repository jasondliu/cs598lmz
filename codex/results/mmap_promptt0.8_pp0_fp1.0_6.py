import mmap
# Test mmap.mmap()

# repr bug #21714
o = mmap.mmap(-1, 100)
print(type(eval(repr(o))))
print(o == eval(repr(o)))
print('Hello World!')

# mmap bug #19082
with open(__file__, 'r+') as fp:
    m = mmap.mmap(fp.fileno(), 0)
    m.seek(0)
    print(m.tell())
    m.write('Hello World!\n'.encode('utf8'))
    m.seek(0)
    print(m.readline())

# try to reproduce mmap bug #19082
with open(__file__, 'r+') as fp:
    m = mmap.mmap(fp.fileno(), 0)
    m.seek(0)
    # Test mmap.mmap(int, int, str, mmap.ACCESS_COPY)
    m2 = mmap.mmap(m.fileno(), 0, mmap.MAP_PRIVATE)
