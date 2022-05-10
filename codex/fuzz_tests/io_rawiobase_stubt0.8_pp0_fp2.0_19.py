import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n):
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
            b[:n] = array.array(b'b', data)
        return n

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
