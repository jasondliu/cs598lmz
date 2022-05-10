import mmap
# Test mmap.mmap
m = mmap.mmap(0, 1024)
m[0:10] = b"1234567890"
print(m[0:10])
m.close()

# Test mmap.mmap with file
f = open("/tmp/test.txt", "wb")
f.write(b"1234567890")
f.close()

f = open("/tmp/test.txt", "r+b")
m = mmap.mmap(f.fileno(), 1024)
m[0:10] = b"abcdefghij"
print(m[0:10])
m.close()
f.close()

# Test mmap.mmap with file
f = open("/tmp/test.txt", "wb")
f.write(b"1234567890")
f.close()

f = open("/tmp/test.txt", "r+b")
m = mmap.mmap(f.fileno(), 1024)
m[0:10] = b"abcdefghij"
print(m[0:10])

