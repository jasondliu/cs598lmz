import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.buffer = b''

    def read(self, size):
        with open(self.path, 'rb') as f:
            if len(self.buffer) >= size:
                data = self.buffer[:size]
                self.buffer = self.buffer[size:]
            else:
                data = self.buffer
                data += f.read(size - len(data))
                self.buffer = b''

        return data

    def readall(self):
        with open(self.path, 'rb') as f:
            data = f.read()
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
            b[:n] = array.array('b', data)
        return n
