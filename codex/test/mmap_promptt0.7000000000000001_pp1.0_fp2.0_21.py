import mmap
# Test mmap.mmap
mmap.mmap(-1, 0)

# Test mmap.mmap()
m = mmap.mmap(0, 0)

# Test mmap.mmap().__len__()
len(m)

# Test mmap.mmap().__del__()
del m

# Test mmap.mmap().close()
m = mmap.mmap(0, 0)
try:
    m.close()
except Exception as e:
    print(e)
del m

# Test mmap.mmap().flush()
m = mmap.mmap(0, 0)
try:
    m.flush()
except Exception as e:
    print(e)
del m

# Test mmap.mmap().find()
m = mmap.mmap(0, 0)
try:
    m.find(b'a')
except Exception as e:
    print(e)
del m

# Test mmap.mmap().find()
m = mmap.mmap(0, 0)
