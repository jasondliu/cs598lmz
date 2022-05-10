import mmap
# Test mmap.mmap
m = mmap.mmap(0, 32, "test")
m.write("1234567890abcdefghijklmnopqrstuv")
m.seek(0)
