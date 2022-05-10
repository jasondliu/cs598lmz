import io
class File(io.RawIOBase):
    def __init__(self, path):
        self._file = io.open(path, 'rb')

    def read(self, size=-1):
        return self._file.read(size)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)

    def tell(self):
        return self._file.tell()

    def close(self):
        return self._file.close()

class FileReader(object):
    def __init__(self, file):
        self.file = file

    def read(self, size=-1):
        return self.file.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def close(self):
        return self.file.close()

class StreamReader(object):
    def
