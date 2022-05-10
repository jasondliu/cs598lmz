import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        super(File, self).__init__(*args, **kwargs)

    def read(self, n=-1):
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
            b[:n] = array.array('b', data)
        return n

    def write(self, b):
        return self.file.write(b)

    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def close(self):
        return self.file.close()

def open(file, mode="r", buffering=-1, encoding=None
