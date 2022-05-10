import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        super().__init__()
        self.close_file = 1
        self.file = file
        self.mode = mode
        self.name = file.name
        self.softspace = file.softspace
        self.readable = self.writable = self.seekable = 0
        if self.mode == 'r' or self.mode == 'rb':
            self.readable = 1
        elif self.mode == 'w' or self.mode == 'wb':
            self.writable = 1
        self.seekable = self.file.seekable()

    def seek(self, ofs, whence=0):
        if not self.seekable:
            raise ValueError('Seek not allowed on this File')
        return self.file.seek(ofs, whence)

    def tell(self):
        if not self.seekable:
            raise ValueError('Tell not allowed on this File')
        return self.file.tell()

    def close(self):
        if self.close_file:

