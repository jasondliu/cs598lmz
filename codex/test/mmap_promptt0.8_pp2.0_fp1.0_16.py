import mmap
# Test mmap.mmap (which has mmap.mmap(fd, ...) signature)
m = mmap.mmap(-1, 128)
m[0:10] = b'abcdefghij'
m.find(b'ab')
# Test mmap.mmap (which has mmap.mmap(fd, length) signature)
m = mmap.mmap(0, 128)
m[0:10] = b'abcdefghij'
m.find(b'ab')
# Test io.open
f = io.open(b"hello", "w")
f.write(b"world")
f.close()
f = io.open(b"hello", "w")
f.write(u"world")
f.close()
f = io.open(b"hello", "w")
f.write(u"world".encode("utf-8"))
f.close()
# Test io.BytesIO
f = io.BytesIO()
f.write(b'Hello, world!')
f.close()
f = io.BytesIO()
