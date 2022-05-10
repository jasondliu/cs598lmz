import io
class File(io.RawIOBase):
    def __init__(self, data=b''):
        self.data = data
    def read(self, size=-1):
        if size == -1:
            return self.data
        else:
            return self.data[:size]
    def readable(self):
        return True
    def writeable(self):
        return False
    def writable(self):
        return False
    def seekable(self):
        return False
</code>

