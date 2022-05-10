import io
class File(io.RawIOBase):
    def __init__(self, fh):
        self.file = fh
        self.encoding = 'utf-8'
        self.errors = 'strict'
        self.newlines = None

    def close(self):
        self.file.close()

    def readable(self):
        return self.file.readable()

    def seekable(self):
        return self.file.seekable()

    def writable(self):
        return self.file.writable()

    def fileno(self):
        return self.file.fileno()

    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def read(self, size=-1):
        return self.file.read(size)

    def write(self, data):
        return self.file.write(data)

    def flush(self):
        return self.file.flush()

class StringIO(io.StringIO):
    def __init__(self, str
