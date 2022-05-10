import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return False
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()

def open(file, mode='rb', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
    if mode == 'r':
        mode = 'rb'
    if mode == 'w':
        mode = 'wb'
    if mode == 'a':
        mode = 'ab'
    if buffering == -1:
        buffering = 65536
    file = builtins.open(file, mode, buffering, encoding, errors, newline, closefd)
    return File(file)
