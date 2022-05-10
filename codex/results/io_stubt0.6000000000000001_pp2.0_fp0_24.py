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
del File
print(view)

# The file object is still alive and can be used to read data
# into the buffer via its readinto method.

print(view[0])

# However, the file object has been destroyed and cannot be used
# to read data into the buffer via its readinto method.

f = io.BufferedReader(File())
f.readinto(view)
del f
del File
print(view)
