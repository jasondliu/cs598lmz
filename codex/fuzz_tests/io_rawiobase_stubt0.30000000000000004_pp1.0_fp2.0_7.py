import io
class File(io.RawIOBase):
    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self.file = None
        self.open()
    def open(self):
        self.file = open(self.file_path, self.mode)
    def close(self):
        self.file.close()
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, n):
        self.file.seek(n)
    def tell(self):
        return self.file.tell()
    def write(self, s):
        return self.file.write(s)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
class File2(io.BufferedIOBase):
    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self
