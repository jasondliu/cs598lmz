import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n = -1):
        return self.file.read()
    def readall(self):
        return self.file.read()
    def readable(self):
        return True
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', data)
        return n

class StringIO(io.StringIO):
    def read(self, n=-1):
        return super().read(n).encode("latin-1")
    def readall(self):
        return self.getvalue().encode("latin-1")
    def readline(self, length=None):
        return super().readline(length).encode("latin-1")
