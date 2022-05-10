import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf

    def readinto(self, b):
        n = len(b)
        if n > len(self.buf):
            n = len(self.buf)
        b[:n] = self.buf[:n]
        self.buf = self.buf[n:]
        return n

    def readable(self):
        return True

class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw

    def readinto(self, b):
        return self.raw.readinto(b)

    def readable(self):
        return True

class MyBufferedReader(io.BufferedReader):
    def __init__(self, raw):
        io.BufferedReader.__init__(self, raw)

class MyBufferedWriter(io.BufferedWriter):
    def __init__(self, raw):
        io.BufferedWriter
