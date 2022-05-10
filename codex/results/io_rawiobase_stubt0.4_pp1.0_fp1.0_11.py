import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self.file = file
        self.mode = mode
        self.closefd = closefd

    def read(self, n=-1):
        return self.file.read(n)

    def write(self, b):
        return self.file.write(b)

    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def fileno(self):
        return self.file.fileno()

    def close(self):
        if self.closefd:
            self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

def open(file, mode='r', closefd=True):
    return File(file, mode, closefd)

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main
