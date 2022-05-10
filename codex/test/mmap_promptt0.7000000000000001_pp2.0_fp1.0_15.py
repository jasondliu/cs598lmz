import mmap
# Test mmap.mmap() for a read-only file
f = open("a.txt", "r+")
f.write("This is a test")
f.close()
