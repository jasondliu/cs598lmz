import io
class File(io.RawIOBase):
    def __init__(self, file_like):
        self.buffer = file_like
        self.length = int(self.buffer.headers['Content-Length'])
        self.bytes_read = 0
    def readable(self):
        return True
    def _read_chunk(self, size=None):
        if size is None:
            size = self.length - self.bytes_read
        data = self.buffer.read(size)
        self.bytes_read += len(data)
        return data
    def readinto(self, b):
        data = self._read_chunk(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', data)
        return n
    def read(self, n=None):
        if n is None:
            n = self.length
        return self._read_chunk(
