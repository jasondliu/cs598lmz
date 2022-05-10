import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        super().__init__(*args, **kwargs)

    def readinto(self, b):
        return self.file.readinto(b)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def read(self, n=-1):
        return self.file.read(n)

    def read1(self, n=-1):
        return self.file.read1(n)

    def close(self):
        return self.file.close()

class FileWrapper(object):
    def __init__(self, file):
        self.file = file

    def __getattr__(self, name):
        return getattr(self.file, name)
