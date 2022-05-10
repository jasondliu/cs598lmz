import io
class File(io.RawIOBase):
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = None
        self.offset = 0
        self.size = os.path.getsize(filepath)
    def read(self, size=-1):
        if not self.file:
            self.file = open(self.filepath, 'rb')
            self.file.seek(self.offset)
        data = self.file.read(size)
        self.offset += len(data)
        return data
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.size + offset
        else:
            raise ValueError('Invalid value for whence')
        if self.file:
            self.file.close()
            self.file = None
    def tell(self):
        return self.offset
