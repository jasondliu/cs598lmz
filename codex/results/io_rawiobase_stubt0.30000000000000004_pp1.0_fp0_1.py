import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
        self.closed = False
        self.mode = file.mode
        self.name = file.name
        self.encoding = file.encoding
        self.errors = file.errors
        self.newlines = file.newlines
        self.line_buffering = file.line_buffering
        self.softspace = file.softspace
        self.buffer = file.buffer
    def close(self):
        self.file.close()
        self.closed = True
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        self.file.flush()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return self.file.readable()
    def readline(self, size=-1):
        line = self.file.readline(size)
        self.offset += len(line)
        return line
    def readlines(self, hint=-
