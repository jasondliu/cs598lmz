import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path=path
    def read(self, size=-1):
        with open(self.path, 'rb') as f:
            return f.read(size)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        with open(self.path, 'rb') as f:
            f.seek(offset, whence)
    def tell(self):
        with open(self.path, 'rb') as f:
            return f.tell()
</code>
This should work.

