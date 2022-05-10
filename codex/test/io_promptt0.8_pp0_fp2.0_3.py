import io
# Test io.RawIOBase
class RawBuffer(io.RawIOBase):

    def __init__(self, value=b''):
        self.buf = value
        self.position = 0

    def tell(self):
        return self.position

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.position = offset
        elif whence == io.SEEK_CUR:
            self.position += offset
        elif whence == io.SEEK_END:
            self.position = len(self.buf) + offset
        else:
            raise ValueError('Invalid value for whence')
        return self.position

    def read(self, size=-1):
        if size is None:
            size = -1
        if size < 0:
            value = self.buf[self.position:]
            self.position = len(self.buf)
            return value
        else:
            if self.position + size > len(self.buf):
                raise EOFError
