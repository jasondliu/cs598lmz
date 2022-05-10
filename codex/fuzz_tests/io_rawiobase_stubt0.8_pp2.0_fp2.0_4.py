import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast('B')
        while n > 0:
            r = self.file.readinto(view)
            view = view[r:]
            n -= r
            if r == 0:
                raise EOFError
        return len(b)

class LineReader(io.RawIOBase):
    def __init__(self, file, buffer_size=io.DEFAULT_BUFFER_SIZE):
        self.file = file
        self.buffer_size = buffer_size
        self.buf = bytearray(buffer_size)
        self.start = 0  # start of valid data in buf
        self.end = 0  # end of valid data in buf
        self.finished = False

    def readable(self):
        return True

    def _fill(self):
        if self.finished:
            return b''  # EOF
        assert self.start == self.end, '
