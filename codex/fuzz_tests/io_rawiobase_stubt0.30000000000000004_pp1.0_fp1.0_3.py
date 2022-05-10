import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def open(self):
        if self.file is None:
            self.file = open(self.filename, 'rb')
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def readable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        self.open()
        return self.file.readinto(b)
    def seek(self, offset, whence=0):
        self.open()
        return self.file.seek(offset, whence)
    def tell(self):
        self.open()
        return self.file.tell()
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    def __del__(self):
        self.close()

def
