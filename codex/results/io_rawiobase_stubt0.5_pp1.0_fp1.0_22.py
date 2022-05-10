import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def open(self):
        self.file = open(self.filename, 'rb')
    def read(self, size=-1):
        return self.file.read(size)
    def close(self):
        self.file.close()
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def flush(self):
        pass
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return False
    def __iter__(self):
        return self.file.__iter__()
    def __next__(self):
        return self.file.__next__()
    def __enter__(self):
        return self
   
