import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'rb')

    def read(self, size=-1):
        return self.file.read(size)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def close(self):
        return self.file.close()

class FileReader(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'rb')
        self.buffer = b''
        self.buffer_size = 4096

    def read(self, size=-1):
        if size == -1:
            return self.readall()
        if size == 0:
            return b''
        if size < len(self.buffer):
            data = self.buffer
