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
view

# Issue #10114
import io

class MyBytesIO(io.BytesIO):
    def __init__(self):
        io.BytesIO.__init__(self, b"abc")

f = MyBytesIO()
f.read(1)
f.close()
