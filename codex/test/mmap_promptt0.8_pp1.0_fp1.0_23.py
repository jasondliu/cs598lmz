import mmap
# Test mmap.mmap() without len = 0
m = mmap.mmap(-1, 0)

# Test mmap.mmap(fileno)
f = open("testfile", "w+")
f.write("Hello Python!\n")
f.flush()
m = mmap.mmap(f.fileno(), 0)
