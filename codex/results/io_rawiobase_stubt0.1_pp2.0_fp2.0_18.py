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
        self.buffer = None
        self.tell = file.tell
        self.seek = file.seek
        self.fileno = file.fileno
        self.flush = file.flush
        self.isatty = file.isatty
        self.readable = 'r' in mode
        self.writable = 'w' in mode
        self.seekable = True
        self.read = file.read
        self.write = file.write
        self.readline = file.readline
        self.readlines = file.readlines
        self.writelines = file.writelines
        self.close = file.close
        self.truncate = file.truncate
        self.__next__
