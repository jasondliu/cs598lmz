import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
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
    def close(self):
        self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()
</code>

