import mmap
# Test mmap.mmap() function.
m = mmap.mmap(-1, 1024)
m.write(b"Hello world!")
m.seek(0)
print(m.read(16))
m.close()

# Test mmap.open() function.
m = mmap.open("test.py")
print(len(m))
print(m.size())
m.close()

# Test mmap.mmap() map creation.
m = mmap.mmap(-1, 1024)
m.write(b"Hello world!")
m.seek(0)
m[6:11] = b"planet"
m.seek(0)
print(m.read(16))
m.close()

# Test mmap.mmap() copy-on-write.
m = mmap.mmap(-1, 1024)
m[:] = b"Hello world!"
m1 = mmap.mmap(m.fileno(), 1024)
m1[:] = b"Foo bar"
m1.seek(0)
m.seek(0)
print("Same:
