import mmap
# Test mmap.mmap().size
with open(filename, 'wb') as f:
    f.write(b'x' * 8192)
    f.write(b'y' * 4096)
    f.write(b'z' * 4096)
m = mmap.mmap(f.fileno(), 0)
print(m.size())
m.close()
# Test mmap.mmap().seek()
with open(filename, 'wb') as f:
    global fsize
    f.write(b'x' * 8192)
    fsize = f.tell()
    f.write(b'y' * 4096)
    fsize2 = f.tell()
m = mmap.mmap(f.fileno(), 0)
print(m.size())
print(m.tell())
print(m.seek(100, 1))
print(m.tell() == 100 + fsize)
print(m.seek(fsize+5, 0))
print(m.tell() == fsize+5)
print(m.seek(0, 2))
