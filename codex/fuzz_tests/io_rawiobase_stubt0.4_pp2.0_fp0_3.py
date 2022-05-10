import io
class File(io.RawIOBase):
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = None
        self.pos = 0
    def open(self):
        self.file = open(self.filepath, 'rb')
        self.pos = self.file.tell()
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.file.seek(offset)
        elif whence == io.SEEK_CUR:
            self.file.seek(self.pos + offset)
        elif whence == io.SEEK_END:
            self.file.seek(0, io.SEEK_END)
            end = self.file.tell()
            self.file.seek(end + offset)
        self.pos = self.file.tell()
    def tell(self):
        return self.pos
    def close(self):
        self.file.close()
        self.file = None
        self.pos = 0
    def readinto(self, b):
       
