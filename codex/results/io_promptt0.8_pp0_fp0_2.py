import io
# Test io.RawIOBase with a C implementation of io.IOBase.
# We need to be careful not to access any internals of the object, as it doesn't
# inherit from object.
class RawIO(io.RawIOBase):
    def readinto(self, b):
        b[0] = ord('s')
        b[1] = ord('p')
        b[2] = ord('a')
        b[3] = ord('m')
        return 4

io.TextIOWrapper(RawIO()).read()

io.BytesIO.write(b'bar')
io.BytesIO.getvalue()
io.BytesIO.tell()
io.BytesIO.tell()
io.BytesIO.seek(0)
io.BytesIO.tell()
io.BytesIO.truncate()
io.BytesIO.tell()
io.BytesIO.truncate(0)
io.BytesIO.tell()
io.BytesIO.truncate(100)
io.BytesIO.tell()
io.BytesIO.truncate(-100)
io.BytesIO.tell
