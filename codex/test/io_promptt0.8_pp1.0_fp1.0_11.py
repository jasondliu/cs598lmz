import io
# Test io.RawIOBase by using it to implement a buffered I/O interface
class BufferedIO(io.RawIOBase):
    def __init__(self, raw):
        self.raw = raw
        self.buffer = ''
    def read(self, n=-1):
        if n >= 0:
            while len(self.buffer) < n:
                data = self.raw.read(n - len(self.buffer))
                if not data:
                    break
                self.buffer += data
        data = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return data
    def readinto(self, b):
        data = self.read(len(b))
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
        self.flush()
        return self.raw
