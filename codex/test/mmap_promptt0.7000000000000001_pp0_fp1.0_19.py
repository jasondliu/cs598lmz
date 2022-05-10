import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 13)
m.write(b"Hello, World!")
print(m[:])
m.close()

del m

# Test mmap.mmap.__new__()
m = mmap.mmap(-1, 13)
m.write(b"Hello, World!")
m[0:5] = b"Hai!"
print(m[:])
m.close()

del m

# Test mmap.mmap.seek()
with open("mmap_test1.dat", "w+") as f:
    f.write("Hello, World!")

m = mmap.mmap(f.fileno(), 0)
print(m.read(1))
m.seek(5)
print(m.read(1))
m.seek(5, 0)
print(m.read(1))
m.seek(0, 2)
print(m.tell())
m.seek(-5, 2)
print(m.read(1))
m.close()

# Test
