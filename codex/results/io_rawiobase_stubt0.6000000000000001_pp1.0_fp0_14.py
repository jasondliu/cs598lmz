import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.mode = mode
        self.name = path
        self.fp = open(path, mode)

    def read(self, size=-1):
        return self.fp.read(size)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return self.fp.seek(offset, whence)

    def readinto(self, b):
        data = self.fp.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n

    def readable(self):
        return True

    def writable(self):
        return True

    def write(self, b):
        return self.fp.write(b)

    def close(self):
        self.fp.close()

    def flush(
