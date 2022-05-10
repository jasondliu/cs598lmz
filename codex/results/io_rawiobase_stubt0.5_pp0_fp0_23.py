import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        if mode not in ('r', 'w'):
            raise ValueError("invalid mode: %r" % mode)
        self._mode = mode
        self._name = name
        if mode == 'r':
            self.f = open(name, 'rb')
        else:
            self.f = open(name, 'wb')

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

    def seek(self, offset, whence=0):
        return self.f.seek(
