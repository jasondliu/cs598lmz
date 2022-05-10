import io
class File(io.RawIOBase):
    def __init__(self, data=None, mode='w+b'):
        self.buf = bytearray()
        if data:
            self.buf += data
        self.readable = 'r' in mode
        sel
