import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.open()
    def open(self):
        self.file = open(self.filename, self.mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, data):
        return self.file.write(data)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    def __iter__(self):
        return self.file.__iter__()
    def __next__(self):
        return self.file.__next__()
    def __getattr__(self, name):
