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
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

def open(file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if isinstance(file, str):
        return io.open(file, mode, buffering, encoding, errors, newline, closefd, opener)
    if buffering == -1:
        buffering = io.DEFAULT_BUFFER_SIZE
    if buffering < 0:
       
