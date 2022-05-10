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

# This is the same as the above, but with a BytesIO instead of a BufferedReader.
f = io.BytesIO(b'\x00')
f.read(1)
del f

# This is the same as the above, but with a TextIOWrapper instead of a
# BufferedReader.
f = io.TextIOWrapper(io.BytesIO(b'\x00'))
f.read(1)
del f

# This is the same as the above, but with a BufferedReader wrapping a
# TextIOWrapper wrapping a BytesIO.
f = io.BufferedReader(io.TextIOWrapper(io.BytesIO(b'\x00')))
f.read(1)
del f

# This is the same as the above, but with a BufferedReader wrapping a
# TextIOWrapper wrapping a BufferedReader wrapping a BytesIO.
f = io.BufferedReader(io.TextIOWrapper(io.BufferedReader(io.BytesIO(b'\x00'))))
f.
