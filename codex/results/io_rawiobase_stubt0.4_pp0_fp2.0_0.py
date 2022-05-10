import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def seekable(self):
        return True

    def readable(self):
        return True

    def writable(self):
        return False

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset = self.offset + offset
        elif whence == io.SEEK_END:
            offset = self.file.size() - offset
        self.offset = offset
        return self.offset

    def tell(self):
        return self.offset

    def readinto(self, b):
        data = self.file.read(self.offset, len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        self.offset += n
        return n
