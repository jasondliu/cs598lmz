import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n
    def write(self, b):
        self.file.write(b)
        return len(b)
    def seek(self, n, whence=io.SEEK_SET):
        self.file.seek(n, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        self.file.close()
    def flush(self):
        self.file.flush()
    def fileno(self):
        return self.file.fileno()
   
