import mmap
# Test mmap.mmap
print(mmap.mmap(-1, 13))

# Test mmap.mmap.size()
print(mmap.mmap(-1, 13).size())

# Test mmap.mmap.tell()
print(mmap.mmap(-1, 13).tell())

# Test mmap.mmap.seek()
print(mmap.mmap(-1, 13).seek(0))

# Test mmap.mmap.read()
print(mmap.mmap(-1, 13).read(13))

# Test mmap.mmap.write()
print(mmap.mmap(-1, 13).write("Hello, World!"))

# Test mmap.mmap.close()
print(mmap.mmap(-1, 13).close())

# Test mmap.mmap.find()
print(mmap.mmap(-1, 13).find("Hello, World!"))

# Test mmap.mmap.rfind()
print(mmap.mmap(-1, 13).rfind("Hello, World!"))

# Test mm
