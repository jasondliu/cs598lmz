import mmap
# Test mmap.mmap()
m = mmap.mmap(0, 1024, 'my_memory', mmap.ACCESS_WRITE)
m.write('hello world')
m.close()
# Test mmap.mmap(-1, ...)
m = mmap.mmap(-1, 1024, 'my_memory', mmap.ACCESS_WRITE)
m.write('hello world')
m.close()
# Test mmap.mmap(0, ..., fileno=f.fileno())
m = mmap.mmap(0, 1024, 'my_memory', mmap.ACCESS_WRITE, fileno=f.fileno())
m.write('hello world')
m.close()
# Test mmap.mmap(-1, ..., fileno=f.fileno())
m = mmap.mmap(-1, 1024, 'my_memory', mmap.ACCESS_WRITE, fileno=f.fileno())
