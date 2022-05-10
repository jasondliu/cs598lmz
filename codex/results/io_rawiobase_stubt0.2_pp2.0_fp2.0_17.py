import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def readinto(self, b):
        data = self.f.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', data)
        return n
    def write(self, b):
        self.f.write(b)
        return len(b)
    def seek(self, pos, whence=0):
        self.f.seek(pos, whence)
    def tell(self):
        return self.f.tell()
    def flush(self):
        self.f.flush()
    def close(self):
        self.f.close()
    def fileno(self):
        return self.f.fileno()
    def __enter
