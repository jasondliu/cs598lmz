import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = io.FileIO(name, mode)
        self.file.seek(0, os.SEEK_END)
        self.size = self.file.tell()
        self.file.seek(0)
        self.buffer = b""
        self.pos = 0
        self.closed = False
    def close(self):
        self.file.close()
        self.closed = True
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return False
    def tell(self):
        return self.pos
    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            self.pos = offset
        elif whence == os.SEEK_CUR:
            self.pos += offset
        elif whence == os.SEEK_END:
            self.pos = self.size + offset

