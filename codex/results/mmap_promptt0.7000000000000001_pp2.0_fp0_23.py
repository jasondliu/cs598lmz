import mmap
# Test mmap.mmap(0, 1)
print(mmap.mmap(-1, 1))

# Test mmap.mmap(-1, 1).close()
print(mmap.mmap(-1, 1).close())

# Test mmap.mmap(-1, 1).close(1)
try: print(mmap.mmap(-1, 1).close(1))
except TypeError: pass

# Test mmap.mmap(-1, 1).find()
try: print(mmap.mmap(-1, 1).find())
except TypeError: pass

# Test mmap.mmap(-1, 1).find('1')
print(mmap.mmap(-1, 1).find('1'))

# Test mmap.mmap(-1, 1).find('1', 0)
print(mmap.mmap(-1, 1).find('1', 0))

# Test mmap.mmap(-1, 1).find('1', 0, 1)
print(mmap.mmap(-1, 1).find('1', 0, 1))

# Test mmap
