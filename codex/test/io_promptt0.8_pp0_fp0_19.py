import io
# Test io.RawIOBase file
class RawIOBase(io.RawIOBase):
    def __init__(self, data=''):
        self.data = data
        self.offset = 0

    def read(self, n=-1):
        print('RawIOBase.read()')
        if n >= 0:
            res = self.data[self.offset:self.offset+n]
            self.offset += n
            return res
        else:
            res = self.data[self.offset:]
            self.offset = 0
            return res

    def seek(self, offset, whence=0):
        print('RawIOBase.seek()')
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = len(self.data) - offset

    def write(self, b: bytes) -> int:
        self.data += b
        self.offset += len(b)
        return len(b)

# Test io.BufferedIOBase file
