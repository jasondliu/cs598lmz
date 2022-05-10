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

class MyBytesIO(io.BytesIO):
    def __init__(self, initial_bytes=None):
        super().__init__()
        if initial_bytes is not None:
            self.write(initial_bytes)
            self.seek(0)

