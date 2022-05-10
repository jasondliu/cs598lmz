import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r', closefd=True, opener=None):
        self.file = io.FileIO(filename, mode, closefd, opener)
        self.buffer = io.BufferedReader(self.file)
        self.read = self.buffer.read
        self.readline = self.buffer.readline
        self.readlines = self.buffer.readlines
        self.write = self.buffer.write
        self.writelines = self.buffer.writelines
        self.seek = self.buffer.seek
        self.tell = self.buffer.tell
        self.close = self.buffer.close
        self.flush = self.buffer.flush
        self.mode = self.buffer.mode
        self.name = self.buffer.name
        self.isatty = self.buffer.isatty
        self.closed = self.buffer.closed
        self.line_buffering = self.buffer.line_buffering
        self.encoding = self.buffer.encoding
        self.errors = self.buffer.errors
       
