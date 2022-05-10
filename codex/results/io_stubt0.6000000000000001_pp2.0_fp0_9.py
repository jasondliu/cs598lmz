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

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedRandom(File())
f.read(1)
del f
view

f = io.BufferedReader(io.BytesIO(b"abcde"))
f.peek(5)
f.peek(5)
f.peek(5)

f.seek(0)
f.peek(5)
f.peek(5)

f.read(1)
f.peek(5)

f.seek(0)
f.read(1)
f.peek(5)

f = io.BufferedReader(io.BytesIO(b"abcde"))
f.peek(0)
f.peek(1)
f.peek(2)

f = io.BufferedReader(io.BytesIO(b"abcde"))
f.seek(1)
f.peek(0)
f
