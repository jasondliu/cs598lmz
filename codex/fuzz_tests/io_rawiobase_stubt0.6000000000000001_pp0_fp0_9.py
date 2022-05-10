import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        with open(name, 'rb') as f:
            self.data = f.read()
    def read(self, size=-1):
        if size == -1:
            return self.data
        else:
            return self.data[:size]
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = len(self.data) - offset
        if self.pos < 0:
            raise ValueError('Negative seek value')
        return self.pos
    def tell(self):
        return self.pos
    def writable(self):
        return False
    def writelines(self, lines):
        raise io.UnsupportedOperation('not writable')
    def flush(self):
        raise io.UnsupportedOperation
