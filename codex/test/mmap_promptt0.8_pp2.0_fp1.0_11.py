import mmap
# Test mmap.mmap()
# https://docs.python.org/2/library/mmap.html

f = open("foo.txt", "w+")
f.write("Hello Python!\nWow, it\'s very interesting.\n")
f.close()

f = open("foo.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
