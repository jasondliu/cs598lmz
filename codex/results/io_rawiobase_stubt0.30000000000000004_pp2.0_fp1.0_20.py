import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode
        self.name = file.name
        self.closed = False
        self.softspace = 0
        self.newlines = None
        self.encoding = None
        self.errors = None
        self.line_buffering = False
        self.seekable = True
        self.readable = True
        self.writable = True
        self.tell = file.tell
        self.seek = file.seek
        self.fileno = file.fileno
        self.flush = file.flush
        self.isatty = file.isatty
        self.read = file.read
        self.readinto = file.readinto
        self.readline = file.readline
        self.readlines = file.readlines
        self.write = file.write
        self.writelines = file.writelines
        self.truncate = file.truncate
        self.close = file.close
        self.closed = file.closed
   
