import io
class File(io.RawIOBase):
    def seek(self, offset, whence=io.SEEK_SET):
        return self.seek(offset, whence)

class FileIOWrapper(io.RawIOBase):
    def __init__(self, file):
        self.file = file

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def read(self, size=-1):
        return self.file.read(size)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def fileno(self):
        return self.file.fileno()

    def flush(self):
        return self.file.flush()

class FileWrapper(io.RawIOBase):
    def __init__(self, file):
        self.file = file

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def read(self, size=-1
