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
del view

# more than 1 chunk
stream = io.BytesIO(b"abcd" * 100)
b = bytearray(8)
stream.readinto(b)
print(b)
stream.seek(0)
stream.readinto(b)
print(b)
