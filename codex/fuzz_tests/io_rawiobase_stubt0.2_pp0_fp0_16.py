import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r"):
        self.file = file
        self.mode = mode
        self.name = getattr(file, "name", None)
        self.closed = False
        self.softspace = 0
        self.newlines = None
        self.encoding = "utf-8"
        self.errors = "strict"
        self.line_buffering = False
        self.write_through = False
        self.buffer = io.BytesIO()
        self.buffer.write(self.file.read())
        self.buffer.seek(0)
    def readable(self):
        return "r" in self.mode
    def writable(self):
        return "w" in self.mode
    def seekable(self):
        return True
    def readinto(self, b):
        return self.buffer.readinto(b)
    def read(self, n=-1):
        return self.buffer.read(n)
    def write(self, b):
        self.buffer.write(b)

