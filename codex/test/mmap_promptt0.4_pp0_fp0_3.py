import mmap
# Test mmap.mmap
print(mmap.mmap(1,1))

# Test mmap.mmap.__enter__
print(mmap.mmap(1,1).__enter__())

# Test mmap.mmap.__exit__
print(mmap.mmap(1,1).__exit__())

# Test mmap.mmap.__getitem__
print(mmap.mmap(1,1).__getitem__(0))

# Test mmap.mmap.__setitem__
print(mmap.mmap(1,1).__setitem__(0,1))

# Test mmap.mmap.close
print(mmap.mmap(1,1).close())

# Test mmap.mmap.find
print(mmap.mmap(1,1).find(b'a'))

# Test mmap.mmap.flush
print(mmap.mmap(1,1).flush())
