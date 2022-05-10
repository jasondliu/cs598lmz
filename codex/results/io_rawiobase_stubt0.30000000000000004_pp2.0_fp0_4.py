import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
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
            b[:n] = array.array('b', data)
        return n

class BytesIO(io.BytesIO):
    def __init__(self, initial_bytes=None):
        io.BytesIO.__init__(self, initial_bytes)
        self.mode = 'rb'
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()
    def close(self):
        if not self.closed:
            io.BytesIO.close(self)
            self.mode = 'rb'
    def flush(self):
        pass
    def fil
