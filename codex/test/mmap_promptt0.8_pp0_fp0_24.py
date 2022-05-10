import mmap
# Test mmap.mmap.read_byte
m = mmap.mmap(-1, 1)
m.write('a')
