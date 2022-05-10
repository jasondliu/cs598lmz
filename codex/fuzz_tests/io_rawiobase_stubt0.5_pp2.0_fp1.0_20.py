import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, pos, whence=0):
        return self.file.seek(pos, whence)
    def tell(self):
        return self.file.tell()
    def fileno(self):
        return self.file.fileno()
    def close(self):
        return self.file.close()

def open(file, mode="r", buffering=-1, encoding=None,
         errors=None, newline=None, closefd=True, opener=None):
    if isinstance(file, io.RawIOBase):
        return file
    if not closefd:
        raise ValueError("Cannot use closefd=False with fileobj")
    if not hasattr(file, "read"):
        raise TypeError("invalid file:
