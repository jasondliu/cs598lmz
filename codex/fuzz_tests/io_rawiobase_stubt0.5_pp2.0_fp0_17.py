import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def readinto(self, buf):
        data = self.f.read(len(buf))
        n = len(data)
        try:
            buf[:n] = data
        except TypeError as err:
            import array
            if not isinstance(buf, array.array):
                raise err
            buf[:n] = array.array(buf.typecode, data)
        return n
    def write(self, b):
        self.f.write(b)
        return len(b)
    def close(self):
        try:
            if self.f is not None:
                self.f.close()
        finally:
            self.f = None
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
