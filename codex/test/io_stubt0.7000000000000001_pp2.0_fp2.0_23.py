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

# b'\x00'

# =========================================================================== #

class ByteCounter(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        self.count = 0
        super(ByteCounter, self).__init__(*args, **kwargs)
    def write(self, b):
        self.count += len(b)
        return len(b)

class File(io.RawIOBase):
    ...

