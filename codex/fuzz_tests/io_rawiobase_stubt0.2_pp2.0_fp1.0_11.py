import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = io.open(self.path, 'rb')
        self.size = os.path.getsize(self.path)
        self.offset = 0

    def read(self, size=-1):
        if size == -1:
            size = self.size - self.offset
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
        return self.offset

    def tell(self):
        return self.offset

    def close(self):
        self.file.close()

class FileReader(io.RawIOBase):

