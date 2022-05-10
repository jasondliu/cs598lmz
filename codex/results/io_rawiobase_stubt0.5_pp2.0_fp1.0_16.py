import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, n=-1):
        return open(self.name, 'rb').read(n)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return False
    def close(self):
        pass
    def __repr__(self):
        return '<File %s>' % self.name

def read(path, mode='rt'):
    if path.endswith('.gz'):
        with gzip.open(path, mode) as f:
            return f.read()
    else:
        with open(path, mode) as f:
            return f.read()

def write(path, data, mode='wt'):
    if path.endswith('.gz'):
        with gzip.open(path, mode) as f:
            f.write(data)
    else:
        with open(path, mode) as f:
            f.write(
