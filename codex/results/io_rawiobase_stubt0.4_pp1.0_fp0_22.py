import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
    def read(self, size=-1):
        with open(self.filename, 'rb') as f:
            return f.read(size)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        with open(self.filename, 'rb') as f:
            f.seek(offset, whence)
    def tell(self):
        with open(self.filename, 'rb') as f:
            return f.tell()
    def close(self):
        pass
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass

def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

def write_file(filename, data, mode='wb'):
    with open(filename, mode) as f:
        f.write(
