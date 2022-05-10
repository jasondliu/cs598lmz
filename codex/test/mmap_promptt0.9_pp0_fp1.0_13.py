import mmap
# Test mmap.mmap class
data = "This is a test string for mmap module."

f = open("mmap_test", "w+")
f.write(data)
f.close()

f = open("mmap_test", "r+")
m = mmap.mmap(f.fileno(), 0)

