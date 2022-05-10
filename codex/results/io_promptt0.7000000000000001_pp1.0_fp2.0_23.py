import io
# Test io.RawIOBase

class MyRawIOBase(io.RawIOBase):

    rawmode = "r"

    def __init__(self, data=""):
        self.data = data
        self.pos = 0
        self.closed = False

    def readable(self):
        return not self.closed

    def seekable(self):
        return False

    def read(self, size=-1):
        if size < 0:
            return self.data[self.pos:]
        newpos = min(self.pos + size, len(self.data))
        ret = self.data[self.pos:newpos]
        self.pos = newpos
        return ret

    def close(self):
        self.closed = True


class MyBufferedRawIOBase(io.BufferedIOBase):

    rawmode = "r"

    def __init__(self, data=""):
        self.raw = MyRawIOBase(data)
        self.buffer = ""
        self.pos = 0

    def close(self):
        self.raw.close()

    def seekable(
