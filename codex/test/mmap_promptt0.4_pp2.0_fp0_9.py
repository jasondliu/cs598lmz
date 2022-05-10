import mmap
# Test mmap.mmap

f = open("/Users/charlie/Desktop/testfile.txt", "w+")
f.write("Hello Python!")
f.close()

f = open("/Users/charlie/Desktop/testfile.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
m.seek(0)
m.write("Hello World!")
