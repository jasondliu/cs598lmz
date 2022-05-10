import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, n=-1):
        return open(self.name, 'rb').read(n)
    def write(self, b):
        with open(self.name, 'wb') as f:
            f.write(b)
    def fileno(self):
        return -1
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        return 0
    def truncate(self, size=None):
        pass
    def readable(self):
        return True
    def writable(self):
        return True
    def flush(self):
        pass
    def close(self):
        pass
    def __repr__(self):
        return '<File %s>' % self.name

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
