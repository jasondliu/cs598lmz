import io
class File(io.RawIOBase):

    def __init__(self, path):
        self.path = path
        self.file = None

    def open(self):
        if self.file is None:
            self.file = open(self.path, 'rb')

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def readable(self):
        return True

    def readinto(self, b):
        self.open()
        return self.file.readinto(b)

    def read(self, n=-1):
        self.open()
        return self.file.read(n)

    def seek(self, offset, whence=io.SEEK_SET):
        self.open()
        return self.file.seek(offset, whence)

    def tell(self):
        self.open()
        return self.file.tell()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def __re
