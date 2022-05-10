import mmap
# Test mmap.mmap()
print(mmap.mmap(1, 1024))

# Test mmap.mmap().tell()
print(mmap.mmap(1, 1024).tell())

# Test mmap.mmap().seek()
print(mmap.mmap(1, 1024).seek(0))

# Test mmap.mmap().read()
print(mmap.mmap(1, 1024).read(1024))

# Test mmap.mmap().write()
print(mmap.mmap(1, 1024).write(b'Hello'))

# Test mmap.mmap().flush()
print(mmap.mmap(1, 1024).flush())

# Test mmap.mmap().close()
print(mmap.mmap(1, 1024).close())

# Test mmap.mmap().size()
print(mmap.mmap(1, 1024).size())

# Test mmap.mmap().rfind()
print(mmap.mmap(1, 1024).rfind(b'\x00'))

