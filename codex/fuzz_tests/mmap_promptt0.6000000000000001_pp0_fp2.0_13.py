import mmap
# Test mmap.mmap.
f = open("test.txt", "r+")
# Size of file must be greater than 0.
f.write("\x00" * 100)
f.flush()
m = mmap.mmap(f.fileno(), 0)
print(m[0:10])
m[0:10] = "0123456789"
m.seek(0)
print(m[0:10])
m.close()
f.close()

# Test mmap.mmap(length).
m = mmap.mmap(-1, 100)
m.write("0123456789")
m.seek(0)
print(m[0:10])
m.close()
