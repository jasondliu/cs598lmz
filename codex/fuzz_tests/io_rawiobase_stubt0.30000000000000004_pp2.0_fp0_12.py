import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode

    def read(self, size=-1):
        return self.file.read(size)

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

    def write(self, b):
        self.file.write(b)
        return len(b)

    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def fileno(self):
        return self.file.fileno()

    def flush(self):
        self.file.flush()

    def
