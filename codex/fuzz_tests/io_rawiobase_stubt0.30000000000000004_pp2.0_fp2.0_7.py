import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        self.f.flush()
    def close(self):
        self.f.close()
    def fileno(self):
        return self.f.fileno()

class _FileIO(io.FileIO):
    def __init__(self, file, mode='r', closefd=True):
        self.file = file
        self.mode = mode
        self.closefd = closefd
        self.closed = False
        self.readable = 'r' in mode
        self.writable = 'w' in mode or 'a' in mode
        self.seekable = True
        self.name = file.name
        self.mode = mode
        self.encoding = None
        self.newlines = None
        self.line_buffering = False
        self.softspace = False
        self.tell()

