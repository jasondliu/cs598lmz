import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def close(self):
        return self.f.close()
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
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def readable(self):
        return True
    def writable(self):
        return False
    def flush(self):
        return self.f.flush()
    def fileno(self):
        return
