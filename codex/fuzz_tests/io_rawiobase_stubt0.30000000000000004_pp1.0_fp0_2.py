import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = io.open(name, 'rb')
        self.size = os.fstat(self.file.fileno()).st_size
        self.read = self.file.read
        self.seek = self.file.seek
        self.tell = self.file.tell
        self.close = self.file.close
        self.closed = self.file.closed
        self.fileno = self.file.fileno
        self.flush = self.file.flush
        self.isatty = self.file.isatty
        self.readable = self.file.readable
        self.readline = self.file.readline
        self.readlines = self.file.readlines
        self.seekable = self.file.seekable
        self.truncate = self.file.truncate
        self.writable = self.file.writable
        self.write = self.file.write
        self.writelines = self.file.writelines
        self.__
