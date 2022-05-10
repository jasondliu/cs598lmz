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

verify_type(MyBytesIO(), "bytesio")
myio = MyBytesIO(b"hello")
verify_type(myio, "bytesio")
verify(myio.getvalue() == b"hello")

class MyOpen(object):
    def __init__(self, name, mode="r", buffering=-1,
                       encoding=None, errors=None,
                       newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
    def __enter__(self):
        self.io = open(
