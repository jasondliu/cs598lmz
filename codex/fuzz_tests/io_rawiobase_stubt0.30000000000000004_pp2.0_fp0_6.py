import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.file = io.FileIO(filename, mode)
        self.mode = mode
        self.name = filename
        self.closed = False
        self.softspace = 0
        if 'b' in mode:
            self.mode = self.mode.replace('b', '')
    def close(self):
        if not self.closed:
            self.file.close()
            self.closed = True
    def flush(self):
        self.file.flush()
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return 'r' in self.mode
    def readline(self, size=-1):
        return self.file.readline(size)
    def readlines(self, size=-1):
        return self.file.readlines(size)
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)

