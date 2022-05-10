import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)
print(view.obj)

# buf = memoryview(b"abc")
# print(buf)
# print(buf.obj)
# buf.obj = b"def"
# print(buf)
# print(buf.obj)

# buf = memoryview(b"abc")
# print(buf)
# print(buf.obj)
# buf[:] = b"def"
# print(buf)
# print(buf.obj)

# buf = memoryview(b"abc")
# print(buf)
# print(buf.obj)
# buf[0] = b"d"
# print(buf)
# print(buf.obj)
