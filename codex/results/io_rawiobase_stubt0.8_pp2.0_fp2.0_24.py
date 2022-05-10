import io
class File(io.RawIOBase):
    def __init__(self, stream):
        self.stream = stream
        self.len = self.stream.tell()
        self.stream.seek(0)

    def read(self, l):
        if self.stream.tell() + l > self.len:
            l = self.len - self.stream.tell()
        return self.stream.read(l)

    def seekable(self):
        return False

    def readable(self):
        return True

    def writable(self):
        return False

class Chunks(io.RawIOBase):
    def __init__(self, pieces):
        self.pieces = pieces
        self.cur = 0

    def read(self, l):
        if self.cur >= len(self.pieces):
            return b''

        d = self.pieces[self.cur]
        if l < len(d):
            self.pieces[self.cur] = d[l:]
            self.cur += 1
            return d[:l]
        else:
            self.cur += 1
            return d


