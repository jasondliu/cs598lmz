import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = None
    def open(self):
        self.file = open(self.path, "rb")
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def writable(self):
        return False
    def write(self, b):
        raise io.UnsupportedOperation("File is not writable")
    def writelines(self, lines):
        raise io.UnsupportedOperation("File is not writable")
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
   
