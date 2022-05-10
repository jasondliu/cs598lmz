import mmap
# Test mmap.mmap
m = mmap.mmap(-1, 13)
m.write('Hello Python!')
m.seek(0)
