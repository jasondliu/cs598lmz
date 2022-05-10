import mmap
# Test mmap.mmap()

mm = mmap.mmap(-1, 13)
mm.write("hello, world!")

