import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.f = self._open(self.path)

    def _open(self, path):
        return open(path, 'rb')

    def write(self, b):
        raise NotImplementedError

    def readinto(self, b):
        return self.f.readinto(b)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def seek(self, pos, whence=io.SEEK_SET):
        return self.f.seek(pos, whence)

    def tell(self):
        return self.f.tell()

    def close(self):
        return self.f.close()

class ReadableFile(File):
    def writable(self):
        return False

class WritableFile(File):

    def writable(self):
        return True

    def readable(self):
        return False

    def readinto(self, b):
        raise Not
