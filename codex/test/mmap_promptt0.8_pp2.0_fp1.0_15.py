import mmap
# Test mmap.mmap()
f = open(r"C:\Users\haoyu\Desktop\test.txt", "w+")
f.write("test").close()

# open for reading and writing
f = open(r"C:\Users\haoyu\Desktop\test.txt", "r+")
m = mmap.mmap(f.fileno(), 0)

# read contents via standard file methods
print(m.readline())  # read one line
print(m.readline())  # read one line

# read contents via slice notation
print(m[:5])  # read 5 bytes
print(m[6:])  # read everything else

# update content using slice notation;
# note that new content must have same size
m[6:] = " world!\n"
m.flush()
print(m[:])

# close the map
m.close()

# close the file
f.close()

print("\n\n")

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
